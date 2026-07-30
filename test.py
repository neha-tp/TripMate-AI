from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

#res=tavily_search("Best hotels in india")
#print(res)

result = search_flights(" Plan a 5 day trip  ")
print(result)