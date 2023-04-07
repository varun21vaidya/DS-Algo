# Number of Provinces
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an <strong>undirected</strong></span><span style="font-size:18px">&nbsp;graph with <strong>V</strong> vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.</span><br>
<br>
<span style="font-size:18px"><strong>Note: </strong></span> <span style="font-size:18px">A province is a group of <strong>directly </strong>or <strong>indirectly connected</strong> cities and no other cities outside of the group. </span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="position: relative;"><span style="font-size:18px"><strong>Input:
[
 [1, 0, 1],
 [0, 1, 0],
&nbsp;[1, 0, 1]
]
</strong></span><img alt="" src="data:image/png;base64,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"><span style="font-size:18px">
<strong>Output:
</strong>2
<strong>Explanation:</strong>
The graph clearly has 2 Provinces [1,3] and [2]. As city 1 and city 3 has a path between them they belong to a single province. City 2 has no path to city 1 or city 3 hence it belongs to another province.</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<div><span style="font-size:18px"><strong>Example 2:</strong></span></div>

<pre style="position: relative;"><span style="font-size:18px"><strong>Input:
[
&nbsp;[1, 1],
&nbsp;[1, 1]
]
</strong></span><img alt="" src="data:image/png;base64,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"><span style="font-size:18px">
<strong>Output :</strong>
1</span>
<div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>numProvinces()</strong>&nbsp;which takes an integer V and an adjacency matrix adj as input and returns the number of provinces. adj[i][j] = 1, if nodes i and j are connected and adj[i][j] = 0, if not connected.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(V<sup>2</sup>)<br>
<strong>Expected Auxiliary Space:</strong> O(V)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ V ≤ 500</span></p>
</div>