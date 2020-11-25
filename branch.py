threshold = 5
candidate = 5

if candidate > threshold:
    print("candidate is larger")
elif candidate < threshold:
    print("candidate is smaller")
else:
    print("candidate is on par")

# if candidate > threshold or candidate == threshold: # essentially if candidate >= threshold
# if candidate > threshold and candidate < threshold: # essentially if candidate == threshold

# try to avoid nesting too deeply because it makes the code hard to read and understand and follow
if candidate > threshold:
    print("candidate is larger")
    if candidate == threshold:
        print("candidate is on par")

if candidate > threshold:
    pass # usefule when commenting things out for troubleshooting