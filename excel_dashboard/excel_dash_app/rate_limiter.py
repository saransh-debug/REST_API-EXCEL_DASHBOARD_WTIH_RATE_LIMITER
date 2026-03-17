import redis

from rest_framework.response import Response
from rest_framework.exceptions import Throttled


redis_client = redis.StrictRedis(host = "localhost" , port="6379" , db = 0 , decode_responses = True)

def rate_limit(max_requests:int , time_period:int):
    def decorator(func):
        def wrapper(self , request , *args, **kwargs):
            client_id = request.id if request.user.is_authenticated else request.META.get("REMOTE_ADDR")
            path = request.path
            client_key = f"rate_limit:{client_id}:{path}"
            
            curr_req = redis_client.get(client_key)
            print(curr_req)
            if curr_req is None:
                redis_client.set(client_key , 1 , ex = time_period)
            elif int(curr_req)<max_requests:
                redis_client.incr(client_key)
            else :
                retry_after  = redis_client.ttl(client_key)
                raise Throttled(detail = f"Rate limit reached . try after {retry_after} seconds")

            return func(self , request , *args, **kwargs)
        return wrapper
    return decorator