
def display_many(*args):
    for arg in args:
        print(arg)

def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":        
    display_info(Name="Jong", age=30, address="Seoul")
    print(50* "_")
    display_many("Hello", "World", "Python", "Programming")
    