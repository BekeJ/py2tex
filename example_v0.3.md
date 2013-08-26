
The py2tex extension provides magic commands to convert python mathematical
expressions to a nice LaTeX representation when using the IPython notebook. The
following commands are defined <i>%tex</i>, <i>%texnr</i> and <i>%texformat</i>.
<br>
The extension was created to provide an minimalistic alternative for mathcad,
but with the power of python. For that purpose, the <a
href="https://bitbucket.org/kiv/unum/src">unum package</a> is supported to
provide unit aware calculations.

# A first example

In[1]:

```
%load_ext py2tex
```

In[2]:

```
from math import *
```

In[3]:

```
%%tex a = 1.0
b = -1.0
c = -1.0
x_1 = (-b-sqrt(b**2-4*a*c))/(2*a)
x_2 = (-b+sqrt(b**2-4*a*c))/(2*a)
x = x_1
a*x**2+b*x+c
```



$$
$$a = 1.0$$
$$



$$
$$b = -1.0$$
$$



$$
$$c = -1.0$$
$$



$$
$$x_{1} = \frac{- b - \sqrt{b^{2} - 4 \cdot a \cdot c}}{2 \cdot a} = -0.618$$
$$



$$
$$x_{2} = \frac{- b + \sqrt{b^{2} - 4 \cdot a \cdot c}}{2 \cdot a} = 1.618$$
$$



$$
$$x = x_{1} = -0.618$$
$$



$$
$$a \cdot x^{2} + b \cdot x + c = 0.000$$
$$


# More examples

As seen above, underscores in variable names are converted to subscript. If more
than one underscore is used, they will be converted to commas. Known greek
letters will be converted their LaTeX equivalent

In[4]:

```
%%tex a_1 = 2.0
a_1_1 = 3.0
a_1_1_12 = 4.0
zeta = 2*pi
beta_alpha = zeta*2
```



$$
$$a_{1} = 2.0$$
$$



$$
$$a_{1,1} = 3.0$$
$$



$$
$$a_{1,1,12} = 4.0$$
$$



$$
$$\zeta = 2 \cdot \pi = 6.283$$
$$



$$
$$\beta_{\alpha} = \zeta \cdot 2 = 12.566$$
$$


All direct function calls are supported for a conversion. (Eg. sin( ... ) will
be converted but math.sin( ... ) will not be converted. This behaviour might be
changed in the future)

In[5]:

```
%tex z = max(sin(pi/7), cos(pi/3))
```



$$
$$z = \max\left(\sin\left(\frac{\pi}{7}\right), \cos\left(\frac{\pi}{3}\right)\right) = 0.500$$
$$


Custom functions are also supported

In[6]:

```
def f(x,y):
    return x**2+x*y+y**2
```

In[7]:

```
%tex f(2,3)
```



$$
$$\mbox{f}\left(2, 3\right) = 19.000$$
$$


Output of the result is not given when the <i>%texnr</i> (or <i>%%texnr</i> )
command is used.

In[8]:

```
%texnr a=2*3-1
%tex a=2*3-1
```



$$
$$a = 2 \cdot 3 - 1$$
$$



$$
$$a = 2 \cdot 3 - 1 = 5.000$$
$$


# Changing the output format

The output format can be changed with the <i>%texformat</i> command. The
following example will show it's usage:

In[9]:

```
%texformat %.2f
```

In[10]:

```
%tex sin(pi/4)
```



$$
$$\sin\left(\frac{\pi}{4}\right) = 0.71$$
$$


In[11]:

```
%texformat %.10f
```

In[12]:

```
%tex sin(pi/4)
```



$$
$$\sin\left(\frac{\pi}{4}\right) = 0.7071067812$$
$$


In[13]:

```
%texformat %.3e
```

In[14]:

```
%tex pi**50
```



$$
$$\pi^{50} = 7.203 \cdot 10^{24} $$
$$


In[15]:

```
%texformat %.3f
```

# Working with units

The unum units must be loaded. For a detailed explenation see the unum
documentation.

In[16]:

```
from unum.units import m,s,km,J,kg,cm
```

In[17]:

```
%%tex a=1*m/s**2
v_0 = 1.0*m/s
t = 3*s
v_t = v_0+a*t
x_t = v_0*t+a*t**2/2
m_ = 100*kg #m is already defined as a unit
E=m_*v_t**2/2
```



$$
$$a = 1.000\;\:\mbox{m}/\mbox{s}^{2}$$
$$



$$
$$v_{0} = 1.000\;\:\mbox{m}/\mbox{s}$$
$$



$$
$$t = 3.000\;\:\mbox{s}$$
$$



$$
$$v_{t} = v_{0} + \mbox{a} \cdot \mbox{t} = 4.000\;\:\mbox{m}/\mbox{s}$$
$$



$$
$$x_{t} = v_{0} \cdot \mbox{t} + \frac{\mbox{a} \cdot \mbox{t}^{2}}{2} = 7.000\;\:\mbox{m}$$
$$



$$
$$m_{} = 100.000\;\:\mbox{kg}$$
$$



$$
$$E = \frac{m_{} \cdot v_{t}^{2}}{2} = 800.000\;\:\mbox{kg}\cdot\mbox{m}^{2}/\mbox{s}^{2}$$
$$


The last expression is maybe not converted to the wanted unit. A solution would
be:

In[18]:

```
%tex E=m_*v_t**2/2
E = E.asUnit(J)
%tex E
```



$$
$$E = \frac{m_{} \cdot v_{t}^{2}}{2} = 800.000\;\:\mbox{kg}\cdot\mbox{m}^{2}/\mbox{s}^{2}$$
$$



$$
$$E = 800.000\;\:\mbox{J}$$
$$


This requires however lots of typing and mixing of the <i>%tex</i> and
<i>%texnr</i> commands. An easy method is provide by using a #asUnit comment.
For example:

In[19]:

```
%%tex E=m_*v_t**2/2 #asUnit J
v_t #asUnit cm/s
```



$$
$$E = \frac{m_{} \cdot v_{t}^{2}}{2} = 800.000\;\:\mbox{J}$$
$$



$$
$$v_{t} = 400.000\;\:\mbox{cm}/\mbox{s}$$
$$


This command uses the Unum.asUnit() method and will raise an
unum.IncompatibleUnitsError if conversion is not possible.
