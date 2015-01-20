Khan Academy - Alan Pierce

Dev on infrastructure team 
Keeping servers running, designing the right architecture for cheap and fast

Cross-cutting projects.
A/B testing system - running experiments against old websites
Events were done logged, and batch-processed (experiments were logged to not interrupt the user's current action)

Now rebuilds the API. Internal API: rethinking the consistent way these things are built
Working through challenges on the internal end.

#shared about my community app



# Given an array of integers, return the second-greatest element. Examples:
# second_greatest_element([3, 5, 2, 1, 9]) should return 9
# second_greatest_element([5, -2, 7, 8]) should return 8
# second_greatest_element([7]) should return None

second_largest = 5
largest = 7
def second_greatest_element(arr):
  # Write code here.
  largest = None
  second_largest = None
  for val in arr:
    if (largest == None or val >= largest):
      second_largest = largest
      largest = val
    #ensures that the second largest only gets updated when you fail to update the largest
    else:
      if (second_largest == None or val >= second_largest):
        second_largest = val
  return second_largest




# Given an array of integers, return the most frequently-occurring element of
# the array. Examples:
# mode([3, 5, 8, 3]) should return 3
# mode([2, 5, 2, 5]) can return either 2 or 5
# mode([]) should return None
def mode(arr):
  # Write code here.
  most_frequent = None
  most_frequent_count = 0
  freq = {}
  for val in arr:
    if val in freq:
      freq[val] += 1
    else:
      freq[val] = 1
    if (freq[val] > most_frequent_count):
      most_frequent = val
      most_frequent_count = freq[val]
  return most_frequent


# Given an array of integers, return the most frequently-occurring element of
# the array. Your solution must run in constant space, so it may not modify the
# input or use a data structure.
def constant_space_mode(arr):
    # Write code here.
  best_val = None
  best_count = 0
  for cur_val in arr:
    count = 0
    for val in arr:
      if cur_val == val:
        count += 1
    if count > best_count:
      best_val = cur_val
      best_count = count
  return best_val

# Find the largest k-cluster in the given array of integers. A k-cluster is a
# range of integers [i, i + k). For example, the mode of the array is the
# largest 1-cluster. 
# The return value should be the first element of the
# k-cluster. Examples:
# largest_cluster([2, 5, 3, 1, 2, 8, 20, 8], 3) should return 1
1, 1 ,2 ,4 , 5, 5,  
      *        *
k = 3
count = 1 
starting_anchor = 2

1 -> [1, 4)    1, 2, 3






class HttpRequest(object):
    """Contains the information needed to make a particular HTTP request."""


def execute_request(http_request):
    """Run an HTTP request.

    Arguments:
        http_request: An HttpRequest object to run.

    Returns: A dictionary containing the parsed response content.
    """


def list_tables(num_items, token):
    """Create an HTTP request for listing the names of database tables.

    Arguments:
        num_items: The maximum number of table names to return.
        token: A string identifying the starting point, or None if the results
            should start from the beginning.

    Returns: An HttpRequest object for the operation.

    The HTTP response contains the following fields:
        table_names: A list of table names with at most num_items elements.
        next_page_token: A token that can be used to retrieve more results. If
            there are no more results, returns None.
    """


# This code has some problems with it:

# This function should print the name of every table to the console.
def print_all_tables():
  page_size = 100
  token = None
  while True:
    request = list_tables(page_size, token)
    response = execute_request(request)
    for table_name in response['table_names']:
      print table_name
    token = response['next_page_token']
    if token == None:
      break




def start_query_job(query):
    """Create an HTTP request for starting a query job.
    
    A query job usually takes between 2 seconds and 5 minutes to run, so this
    request starts the query job and returns immediately. Use check_job_status
    to determine later if the query was successful. If it was successful, its
    result will be a single string.

    Arguments:
        query: The query string to run.

    Returns: An HttpRequest object for the operation.

    The HTTP response contains the following fields:
        job_id: A unique identifier for the job, or None if there was a problem
            starting the job.
        error: If there was a problem starting the job, an error code
            indicating the problem.

    The possible errors are INVALID_QUERY, TOO_MANY_CONCURRENT_QUERIES,
    INTERNAL_ERROR, and CONNECTION_ERROR.
    """

def check_job_status(job_id):
    """Create an HTTP request for checking the status of a query job.

    Arguments:
        job_id: The job ID to check.

    Returns: An HttpRequest object for the operation.

    The HTTP response contains the following fields:
        state: A string, one of RUNNING, DONE, or ERROR.
        result: If the job is in the DONE state, a string with the job's
            result. Otherwise, this field will be None.
        error: If the job is in the ERROR state, an error code indicating the
            problem. Otherwise, this field will be None.
            
    The possible errors are RESPONSE_TOO_LARGE, QUERY_FAILED, INTERNAL_ERROR,
    and CONNECTION_ERROR.
    """

# This function should run a query, wait for its completion, and return its
# result. You may assume that no errors occur.
def run_job(query):
  request = start_query_job(query)
  job_id = execute_request(request)["job_id"]
  request = check_job_status(job_id)
  
  response = execute_request(request)
  state = response["state"]
  result = response["result"]
  
  while (state == RUNNING)
    request = check_job_status(job_id)
    response = execute_request(request)
    state = response["state"]
    result = response["result"
  return result


