print("What type of cover does the book have?")
cover_type = input()
    
if (cover_type == "soft"):

    print("Is your soft cover book perfect bound?")
    sb = input()
    
    if (sb == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")
 