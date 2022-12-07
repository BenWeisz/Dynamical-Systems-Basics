# Numerical-Integration-Basics

### Preamble

This write up is based on material from **Steve Brunton**'s amazing course on youtube called [Differential Equations and Dynamical Systems](https://www.youtube.com/@Eigensteve). If you haven't seen this series, definitely go check it out, it gives you an intuitive sense for why you should care about dynamical systems, some practical examples and how to solve them.

I'm writing this is part because I forget things that I've learned easily and so this is just a means by which I'm hoping to both give myself a refresher and a resource to come back to later. 

### Motivation

So why should you care about dynamical systems? What a great question! Dynamical systems are all around us, you can see them in action in simple objects and phenomena in your everyday life. The motion of the bobble head on your desk? Dynamical system. The number of cases of Covid19? Dynamical system. The fuel consumption of your car? Dynamical system. Everytime, the rate of change of a variable in time is related to the quantity of the variable at that time you have a dynamical system. These systems give us a new tool for us to place in our modeling toolkits. Alright lets get our hands dirty.

## First Order Linear Differential Equations
<p align="center">
    $\frac{d}{dt}x(t) = \lambda x(t)$
</p>

Wow, what a mouthful of a subtitle. Lets break it down with the above example. The **First Order** part comes from the fact that for the variable that we are concerned with $x(t)$, we only use its first derivative in the equation. The **Linear** part comes from the fact that the expression on the right hand side is a linear function of our variable $x(t)$. And of course because our equation involves the derivative of our variable we have the term **Differential Equation** being used. This type of equation is part of a more general class of equations call **Ordinary Differential Equations** or ODEs for short. We say **Ordinary** because we only use the normal derivatives in our equations and not the partial derivatives. 

As an aside, lets take a look at some simplified notation. The first thing we're going to do is drop the $(t)$ evaluations. We're going to assume that they're still there, but we'll only use that notation when we're actually evaluating them at some value $t=a$.
<p align="center">
    $\frac{d}{dt}x = \lambda x$
</p>

Alright, the last thing we'll do is drop represent $\frac{dx}{dt}$ by $\dot{x}$. If you see double dot notation that just means the second derivative and so on for higher order derivatives. So finally we have:
<p align="center">
    $\dot{x} = \lambda x$
</p>

Lets try to come up with a solution for this equation. But what do we even mean by a solution? Basically we're just trying to figure out what this equation tells us about our variable $x(t)$ as it evolves in time. We are looking for a relation between the dependent variable $x(t)$ and the independent variable $t$ in the form of an equation.

Okay, so at first glance it might look like our equation above doesn't really tell us anything about the variable $x(t)$ in time. This sort of looks like a chicken or the egg scenario. How do we compute the derivative of our variable $x(t)$ if we first need the derivative to define the variable? Kinda odd isn't it?

We have a few options here. We can either try to solve these types of equations by simply manipulating the variables we have, or we can try to approximate the solution the first method might give us. First, we're going investigate the method of manipulating the variables we have; this is what we call an **Analytic Solution**.

## Analytic Solutions
There are many ways to come up with an analytic solution. Let's look at one for now, and we'll look at another method later.

### Method 1: Magic (Sort of)

<p align="center">
    $\dot{x} = \lambda x, \lambda \in \mathbb{R}$
</p>

Let's look at our motivating example first. As we mentioned before this one is a first order ODE. The first thing we ask ourselves is "what functions do I know who's derivative is just a constant times itself." Well, we don't even really need an exact solution at this point, we just need some functions that sort of behave this way. A couple of function classes in our toolkit exhibit this cyclical behaviour when being differentiated. We have functions like $e^t$, $sin(t)$ and $cos(t)$.

For $e^t$ we know it's derivative is equal to itself.

<p align="center">
    $\frac{d}{dt} e^t = e^t$
</p>

This seems like the function we want to be using with the addition that we'll make use of the chain rule. To understand why we won't use $sin(t)$ or $cos(t)$ in this particular situation differentiate $sin(t)$ and notice that no matter the choice for the constant $\lambda$ our differential equation doesn't hold since $\lambda$ only scales $sin(t)$'s amplitude.

Ok so lets play around with $e^t$. Let's say we choose $x(t) = e^t$ as our guess at the solution. If we take its derivative, we end up with the same function. Looking at our differential equation, we are still missing a constant factor of $\lambda$ for the derivative.

<p align="center">
    $\frac{d}{dt} e^t = e^t$
</p>

Let's take a look at how this function's derivative behaves when we modify the exponent. If we add a factor $\lambda$ infront of $t$ we get the following derivative:

<p align="center">
    $\frac{d}{dt} e^{\lambda t} = \lambda e^{\lambda t}$
</p>

Take a hard look, do you see anything interesting? Yup! Its our solution. We take $x(t) = e^{\lambda t}$. Now if we substitute in our function $x(t)$ we have:

<p align="center">
    $\frac{d}{dt} e^{\lambda t} = \frac{d}{dt} x(t) = \lambda x(t) \rightarrow{} \dot{x} = \lambda x$
</p>

If you feel like what you just watched was magic trick then you'd sort of be correct. All that we did is basically just guessed a solution that happened to work for this particular ODE.

### Method 2: Taylor Series
