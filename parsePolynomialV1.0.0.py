# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:03:26 2018

@author: Daniel
"""
import re

def getNumbers(polynomial):
    """ polynomial is a polynomial in the form of a string, e.g. '-10x^5+12x^4+20x-19'
        return: all the coefficients in a polynomial as a list"""
    COEFFICIENT_PATTERN = re.compile(r"(?<!x\^)(?<!x\^-)-?\d+")
    return [int(c) for c in COEFFICIENT_PATTERN.findall(polynomial)]

def getExp(terms):
    """ terms is all the terms of a polynomial expression in the form of a list
        return: all the exponents of the terms in the form of a list"""
    exp = re.compile(r"(?<=\^)([+-]?[0-9])")
    return [int(c) for c in exp.findall(terms)]

def getTerms(equation):
    """ equation is the polynomial in the form of a string. 
        return: the terms of the equation in the form of a list"""
    terms = equation.replace('-','+-').split('+')
    new_terms = []
    for term in terms:
        term = term.replace('-x', '-1*x')
        if term.startswith('x'):
          term = term.replace('x', '1*x')
        if term.endswith('x'):
          term = term.replace('x', 'x^1')
        if term != '':
          new_terms.append(term)
    return new_terms

def getCoefficients(terms):
    """ terms is all the terms of a polynomial expression in the form of a list
        return: all the coefficients of the terms in the form of a list"""    
    coefficients = []
    for term in terms:
      coefficients.append(getNumbers(term))
    return coefficients

def getExponents(terms):
    """ terms is all the terms of a polynomial expression in the form of a list
        getExponents uses getExp to search for the exponents in each index of the list
        return: all the exponents of the terms in the form of a list"""    
    exponents = []
    for term in terms:
        exponents.append(getExp(term))
    return exponents

def formatList(L):
    """ formats each list by removing the square brackets, making a list of lists of strings
        into a list of integers
        return: the formatted list"""
    LFormatted = []
    for i in L:
        if i != []:
            LFormatted.append(int(str(i)[1:-1]))
    return LFormatted

def getNewCoeff(oldCoeff, oldExp):
    """ oldCoeff are the coefficients in the original polynomial expression as a list
        oldExp are the exponents of the original polynomial as a list
        return: the coefficients of the differentiated polynomial as a list"""
    newCoeff = []
    if len(oldCoeff) > len(oldExp):
        for i in range(0,len(oldExp)):
            newCoeff.append(oldExp[i]*oldCoeff[i])
    else:
        for i in range(0,len(oldCoeff)):
            newCoeff.append(oldCoeff[i]*oldExp[i])
    return newCoeff     
  
def getNewExp(oldExp):
    """ oldExp are the exponents of the original polynomial as a list
        return: the exponents of the differentiated polynomial as a list"""
    newExp = []
    for i in oldExp:
        newExp.append(i-1)
    return newExp

def getNewTerms(newCoeff, newExp):
    """ newCoeff are the coefficients of the differentiated polynomial expression as a list
        newExp are the exponents of the differentiated polynomial expression as a list
        return: the new terms of the differentiated polynomial as a list"""
    newTerms = []
    for i in range(0,len(newCoeff)):
        newTerms.append(str(newCoeff[i])+'x^'+str(newExp[i]))
    return newTerms

def formatTerms(terms):
    """ terms are the terms of the differentiated polynomial as a list 
        return: a formatted list of the terms of the differentiated polynomial"""
    new_terms = []
    for term in terms:
      term = term.replace('-1x', '-x')
      term = term.replace('x^0','')
      term = term.replace('^1','')
      if term != '':
        new_terms.append(term)
    return new_terms      

def joinTerms(terms):
    """ terms are the terms of the differentiated polynomial as a list 
        return: the terms of the differentiated polynomial as a string"""
    expression = ''
    for term in terms:
        if str(term)[0] == '-':
            expression += term
        else:
            expression += '+'+term
    if expression[0] == '+':
        expression = expression[1:]
    return expression

def differentiate(expression, showWorkings):
    """
        Synopsis:
                expression is a polynomial expression in the form ax^b+cx^d+...+vx^w+yx^z
                for example a valid equation is -10x^5+12x^4+20x-19
                
                showWorkings is a Boolean and therefore can only have the value of
                either True or False
                
                the output of the function is the derivative of the expression in the form
                ab^(b-1)+cdx^(d-1)+...+vwx^(w-1)+yzx^(z-1) 
                for example a valid derivative is -50x^4+48x^3+20
    """
    terms = getTerms(expression)
    coefficients = getCoefficients(terms)
    exponents = getExponents(terms)

    coeff = formatList(coefficients)
    exp = formatList(exponents)

    newCoeff = getNewCoeff(coeff,exp)
    newExp = getNewExp(exp)   
    
    newTerms = getNewTerms(newCoeff, newExp)   
    formattedTerms = formatTerms(newTerms)
    
    diffExpression = joinTerms(formattedTerms)
    
    if showWorkings == True:
        print('Parsing the polynomial expression...\n')
        print('terms: ',terms)
        print('coeff: ',coeff)
        print('exp: ',exp)
        print('\nWorking out differentiated polynomial...\n')
        print('new coeff: ',newCoeff)
        print('new exp: ',newExp)
        print('new terms: ',newTerms)
        print('formatted terms: ',formattedTerms)
    print('\nderivative of '+expression+' is '+diffExpression)
 
ch = ''
expression = ''
show = True

print('To differentiate a polynomial use the function differentiate(<polynomial>, <True/False>)'
      +'\nwhere polynomial is replaced by the polynomial that you want to differentiate and'
      +'<True/False> is replaced by either T (True) or F (False).')
print('\nPress any other key apart from q to continue (q will exit the program).')

while True:
    ch = input('Press any key... ').lower()
    if ch == 'q':
        break
    else:
        expression = input('expression: ')
        show = input('show workings (T/F): ').upper()
        if show == 'T':
            differentiate(expression,True)
        elif show == 'F':
            differentiate(expression,False)
        else:
            print('Invalid input!')   
