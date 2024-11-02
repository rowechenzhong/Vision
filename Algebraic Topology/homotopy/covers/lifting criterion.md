Let $p: (\tilde{X}, \tilde{x}_0) \to (X, x_0)$ be a covering map, as usual. We are given a map $f: (Y, y_0) \to (X, x_0)$. Then, a ==**lift**== of $f$, $\tilde{f}$, is a map such that $p\circ \tilde{f} = f$ and $\tilde{f}(y_0) = \tilde{x}_0$. The lifting property told us all we need to know about lifting homotopies. Let's see if we can find analogous results for the general case. There are two directions: existence and uniqueness. 
> [!theorem] Lifting Criterion
> Suppose $Y$ is ==*path-connected*== and ==*locally path-connected*==. Then, a lift exists iff $$ f_*(\pi_1(Y, y_0))\subset p_*(\pi_1(\tilde{X}, \tilde{x}_0)) $$ 

The [[unique lifting]] theorem completes this characterization.
 
> [!idea] Conditions
>  
>  -  The $f_*(\pi_1(Y))\subset p_*(\pi_1(\tilde{X}))$ condition is required for all of our loops to lift to loops. 
>  
>  -  ==*Path-connectedness*== is required to construct anything at all. 
>  
>  -  ==*Local path-connectedness*== is required to show our construction is continuous. 
>  
>  

 
> [!proof]-
 First off, if such a lift exists, then $f_* = p_*\circ \tilde{f}_*$, so the inclusion is obvious. For the other direction, well, we already know how to lift paths, and we know that $Y$ is path-connected. Thus, there is exactly one way to proceed: 
> > [!part]-  
>  For any $y$, draw some path $\gamma$ connecting $y_0$ to $y$; this is sent to a path $f\gamma$ connecting $f(y_0) = x_0$ to $f(y)$. This guy lifts to a unique path $\widetilde{f\gamma}$ in $\tilde{X}$ starting at $\tilde{x}_0$. The place where this path ends must be $\tilde{f}(y)$, so let's define it as such. 
> 
>  
> > [!part]- This is well-defined
>  Pick a different path $\gamma'$ from $y_0$ to $y$. Observe that $(f\gamma)\conj{(f\gamma')}$ is a loop in $f_*(\pi_1(Y, y_0))$. Thus, ==*by the condition,*== it must lift to a loop in $\tilde{X}$ based at $\tilde{x}_0$. Staring at the lifts of $f\gamma$ and $f\gamma'$ individually, we conclude that $\widetilde{f\gamma}$ and $\widetilde{f\gamma'}$ end at the same point. **Observe that in general, there will exist a lift of $(f\gamma)\conj{(f\gamma')**$ as a path, but it will not necessarily be a loop.} 
> 
>  
> > [!part]- This is continuous
>  Let $y$ be arbitrary. For any open neighborhood $\tilde{U}$ of $\tilde{f}(y)$, I need to exhibit an open neighborhood $V$ of $y$ such that $\tilde{f}(V)\in \tilde{U}$. Fine, $f(y)$ is evenly covered, so WLOG $\tilde{U}$ is mapped homeomorphically onto $U$ by $p$. Then, $f^{-1}(U)$ is open in $Y$. By ==*local path-connectedness,*== I can pick a path-connected open neighborhood $V\subset f^{-1}(U)$ of $y$. This literally concludes. Like, now pick any $v\in V$. We can draw a path from $y_0$ to $v$ called $\gamma\eta$, where $\gamma$ is a fixed path from $y_0$ to $y$, and $\eta$ is a path from $y$ to $v$. This gets sent to some path $f\gamma f\eta$ which ends in $U$, which lifts to some path $\widetilde{f\gamma} \widetilde{f\eta}$ which ends in $\tilde{U}$. By definition, the ending point is $\tilde{f}(v)$.