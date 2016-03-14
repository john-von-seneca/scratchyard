
def init_base_cases()
	db[graph_1.certificate] = 0
	db[graph_2.certificate] = 1
	db[graph_3__triangle.certificate] = 3
	db[graph_3__vee.certificate] = 2

def chromatic_index(graph)
	conn_components = find_connected_components(graph)
	cis_components = [db[component.certificate] for component in conn_components]
	return max(cis_components)

for n = range(2,N+1):
	for graph in connected_graphs(n):
		cis_current = [chromatic_index(graph \ node) for node in graph.nodes]
		ci_mean_1 = mean(ci+1 for ci in cis_current)
		ci_mean_2 = mean(ci+2 for ci in cis_current)
		ci_max = max(cis_current)
		if((ci_max==mean_1) or (ci_max==mean_2)):
			db[graph.certificate] = ci_max
		else:
			db[graph.certificate] = max(ci_max, ci_mean_1, ci_mean_2)
