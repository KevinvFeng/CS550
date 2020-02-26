# Problem 2
__前提假设__
这是一个二维平面
__证明__
1. 设$m,n,g$在平面上,坐标分别为$[x_m,y_m],[x_n,y_n],[x_g,y_g]$
2. $$\begin{aligned}
cost(m,n)&=2*Manhattan(m,n)\\
&=2*(abs(x_m-x_n)+abs(y_m-y_n))
\end{aligned}$$
3. $$\begin{aligned}
    h(n) &= Manhattan(n,g)\\
    &=abs(x_g-x_n)+abs(y_g-y_n)
    \end{aligned}$$
4. $$\begin{aligned}
    h(m) &= Manhattan(m,g)\\
    &=abs(x_g-x_m)+abs(y_g-y_m)
    \end{aligned}$$
5. $$\begin{aligned}\therefore 
    &h(n)-h(m) = \\
    &abs(x_g-x_n)+abs(y_g-y_n) - abs(x_g-x_m) - abs(y_g-y_m)
 \end{aligned}$$
6. 对于 $x_n\le x_g \le x_m$
   1. $abs(x_g-x_n)+abs(x_g-x_m) = abs(x_m-x_n) $
   2. $\because abs(x_g-x_m)\ge 0$
   3. 所以$abs(x_g-x_n)+abs(x_g-x_m) \le abs(x_m-x_n)$
7. 对于 $x_n,x_m在x_g$同侧时
   1. $abs(x_g-x_n) - abs(x_g-x_m) = \pm x_m-x_n \le abs(x_m-x_n)$
8. $\therefore h(n)-h(m) \le abs(x_m-x_n)+abs(y_g-y_n) \le 2*(abs(x_m-x_n)+abs(y_m-y_n))$
9. $\begin{aligned}h(n)-h(m) \le cost(m,n)\\
    h(n)\le cost(m,n)+h(m)
\end{aligned}$
10. consist