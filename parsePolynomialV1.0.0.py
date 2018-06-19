# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:03:26 2018

@author: Daniel
"""
import re

def getNumbers(polynomial):
  COEFFICIENT_PATTERN = re.compile(r"(?<!x\^)(?<!x\^-)-?\d+")
  return [int(c) for c in COEFFICIENT_PATTERN.findall(polynomial)]

def getExp(terms):
  exp = re.compile(r"(?<=\^)([+-]?[0-9])")
  return [int(c) for c in exp.findall(terms)]

def getTerms(equation):
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
    coefficients = []
    for term in terms:
      coefficients.append(getNumbers(term))
    return coefficients

def getExponents(terms):
    exponents = []
    for term in terms:
        exponents.append(getExp(term))
    return exponents

def formatList(L):
    LFormatted = []
    for i in L:
        if i != []:
            LFormatted.append(int(str(i)[1:-1]))
    return LFormatted

def getNewCoeff(oldCoeff, oldExp):
    newCoeff = []
    if len(oldCoeff) > len(oldExp):
        for i in range(0,len(oldExp)):
            newCoeff.append(oldExp[i]*oldCoeff[i])
    else:
        for i in range(0,len(oldCoeff)):
            newCoeff.append(oldCoeff[i]*oldExp[i])
    return newCoeff     
  
def getNewExp(oldExp):
    newExp = []
    for i in oldExp:
        newExp.append(i-1)
    return newExp

def getNewTerms(newCoeff, newExp):
    newTerms = []
    for i in range(0,len(newCoeff)):
        newTerms.append(str(newCoeff[i])+'x^'+str(newExp[i]))
    return newTerms

def formatTerms(terms):
    new_terms = []
    for term in terms:
      term = term.replace('-1x', '-x')
      term = term.replace('x^0','')
      term = term.replace('^1','')
      if term != '':
        new_terms.append(term)
    return new_terms      

def joinTerms(terms):
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
        print('terms: ',terms)
        print('coeff: ',coeff)
        print('exp: ',exp)
        print('new coeff: ',newCoeff)
        print('new exp: ',newExp)
        print('new terms: ',newTerms)
        print('formatted terms: ',formattedTerms)
    
    print('derivative of '+expression+' is '+diffExpression)