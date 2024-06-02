# Network Flow

* Grows out of bipartite matching
  * *bipartite* graph is an undirected graph whose node set can be partitioned as V = X U Y,
  s.t. every edge e $\epsilon$ E has one end in X and the other end in Y. 
  
  * Matching in this problem is a collection of pairs over the set s.t. no element of the set appears in more than one pair. 
    * The edges constitute pairs of nodes, and we say that a *matching* in a graph G = (V, E) is a set of edges M \subset E with the property that each node appears in at most one edge of M. A set of edges is a perfect matching if every node appears in exactly one edge of M.

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
  * Given flow network G and flow f on G, we define the residual Graph G~f~ of G with respect to f as follow: 
    * The node set of G~f~ is the same as G's
    * For each edge e = (u,v) of G on which f(e) < c~e~, there are c~e~ - f(e) "leftover" units of capacity on which we could try pushing flow forward. So we include the edge e = (u,v) in G~f~, with a new capacity of c~e~ - f(e).
      * The edges included this way called *forward edges*
    * For each edge e = (u,v) of G on which f(e) > 0, there are f(e) units of flow that we can undo if we want to
      * Achieve this by pushing flow backward!
      * Include the edge $e^{\prime}^ = (v,u)$ in G~f~ with a capacity of f(e)
      * e^\prime^ has the same ends as e, but its direction is the opposite and so its a *backward edge*
