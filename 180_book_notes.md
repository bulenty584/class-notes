# Network Flow

* Grows out of bipartite matching
  * *bipartite* graph is an undirected graph whose node set can be partitioned as V = X U Y,
  s.t. every edge e $\epsilon$ E has one end in X and the other end in Y. 
  
  * Matching in this problem is a collection of pairs over the set s.t. no element of the set appears in more than one pair. 
    * The edges constitute pairs of nodes, and we say that a *matching* in a graph G = (V, E) is a set of edges M $\subset$ E with the property that each node appears in at most one edge of M. A set of edges is a perfect matching if every node appears in exactly one edge of M.

## Formulating the Problem

* Network models have several aspects:
  * capacities on the edges that say how much they can carry
  * source nodes in the graph which generate traffic
  * sink/destination notes which can "absorb" traffic if it arrives
  * traffic itself, which is transmitted across edges
  
* Three assumptions have to be made about flow networks:
  * no edge enters the source node s, and no edge leaves the sink node t
  * There is at least one edge incident to each node
  * All capacities are integers
  
* Defining Flow
  * s-t flow is a function *f* that maps each edge e to a nonnegative real number
    * The value f(e) represents the amount of flow carried by edge e. A flow *f* must satisfy the following: 
	  * Capacity must be positive
	  * For each node other than s and t, the sum of the capacities going into the node must equal the sum of the capacities going out of that node

* Max-Flow problem is thus to find a flow of maximum possible value

* Suppose we cut the nodes of a graph into two sets A and B so that s $\epsilon$ A and t $\epsilon$ B.
  * Any flow that goes from s to t must cross from A into B at some point and use some edge capacity from A to B
    * Each cut of the graph puts a bound on the maximum possible flow value

## Short Review of MaxFlow

### Parameters

* Each edge has a positive capacity of how much flow they can carry
* We have a sink node that only has edges directed into it and a source node that has edges out of it
* We define flow as the amount of flow out of the source node
* At each node, we must have a conservation of flow (flow in = flow out)

### Designing the Algo

* How we push flow
  * We can have *forwards* and *backwards* edges!
    * To "undo" flow
      * Push forward on edges with leftover capacity and push backward on edges that already carry flow
      
* Residual Graph 
  * Given flow network G and flow f on G, we define the residual Graph G<sub>f</sub> of G with respect to f as follow: 
    * The node set of G<sub>f</sub> is the same as G's
    * For each edge e = (u,v) of G on which f(e) < c<sub>e</sub>, there are c<sub>e</sub> - f(e) "leftover" units of capacity on which we could try pushing flow forward. So we include the edge e = (u,v) in G<sub>f</sub>, with a new capacity of c<sub>e</sub> - f(e).
      * The edges included this way called *forward edges*
    * For each edge e = (u,v) of G on which f(e) > 0, there are f(e) units of flow that we can undo if we want to
      * Achieve this by pushing flow backward!
      * Include the edge e<sup>'</sup> = (v,u) in G<sub>f</sub> with a capacity of f(e)
      * e<sup>'</sup> has the same ends as e, but its direction is the opposite and so its a *backward edge*

* Precise way we push flow from s to t in a residual graph
  * Let P be a simple s-t path in G<sub>f</sub>
  * define *bottleneck(P,f)* to be the **minimum** residual capacity of any edge on P wrto flow f
  
  ```
  augment(f,P):
      Let b = bottleneck(P,f)
      for each edge (u,v) in P:
        If e = (u,v) is a forward edge then
            increase f(e) in G by b
        Else ((u,v) is a backward edge, and let e = (v,u))
            decrease f(e) in G by b
        Endif
      Endfor
      Return(f)
      
  ```
  
  * Line-by-line
    * First we find the minimum residual capacity on any path from s to t with a flow
    * we then loop over every edge in the path
    * If the edge is a forward edge which we defined above!
      * increase the capacity in the graph by the bottleneck
    * If the edge is a backward edge, then decrease the capacity of the backward edge by bottleneck 
    
* Now we can define the max-flow algo

```
Initially f(e) = 0 for all e in G
While there is an s-t path in the residual graph:
    Let P be a simple s-t path in the residual graph
    f_prime = augment(f,P)
    update f to be f_prime
    update the residual graph to be the residual graph with f_prime
Endwhile
Return(f)
```

# 6.4 KnapSack Problem




    
