from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

#res=tavily_search("Best hotels in india")
#print(res)

#result = search_flights(" Plan a 5 day trip  ")
#print(result)

user_input=input("Enter travel request:")
res=run_travel_agent(user_input, thread_id="test_user")
print(res["answer"])