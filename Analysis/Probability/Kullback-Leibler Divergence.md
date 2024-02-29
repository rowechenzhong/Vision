>[!definition] KL Divergence
>The ==**KL Divergence**== of two discrete probability distributions $P,Q$ over sample space $\abs{\mathcal{X}} < \infty$ is 
>$$D\left(P |Q \right) = \sum_{x\in \mathcal{X}} P(x) \log\left(\frac{P(x)}{Q(x)}\right)$$

So long as $Q$ is supported everywhere, this is a strictly convex function of $P$ minimized globally at $P = Q$.