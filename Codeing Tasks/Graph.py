#!/usr/bin/env python
# coding: utf-8

# In[28]:


graph = {}

def addEdge(graph,node,edge):
        if not edge in graph.keys():
            graph[edge] = []
        graph[node].append(edge)
        return graph

def addnode(graph,node,edges):
    graph[node] = []
    for edge in edges:
        if not edge in graph.keys():
            graph[edge] = []
        graph[node].append(edge)

    return graph

graph = addnode(graph,"a",["b","c","f"])
graph = addEdge(graph,"c","f")
#addEdge(graph,'a','c')
addEdge(graph,'b','c')
addEdge(graph,'b','e')
addEdge(graph,'c','d')
addEdge(graph,'c','e')
addEdge(graph,'c','a')
addEdge(graph,'c','b')
addEdge(graph,'e','b')
addEdge(graph,'d','c')
addEdge(graph,'e','c')


# In[29]:


print(graph)


# In[30]:


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath


# In[31]:


print(find_path(graph,"c","b"))


# In[32]:


def find_all_paths(graph, start, end, path =[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths


# In[33]:


print(find_all_paths(graph, 'd', 'c'))

