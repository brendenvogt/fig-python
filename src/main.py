
# receiving resources
# resources are in json format
# resources have the following main parts:
#   apiVersion
#   kind
#   metadata
#   spec

# a resource's apiVersion allows this spec to evolve as necessary
# a resource kind marks this file to be received and consumed in a specific way.
# a resource's metadata contains information such as: name, labels
# a resource spec is application specific and its definition is up to the consumer. 

from samples.v1 import CONFIG_MAP

def main():
    c = CONFIG_MAP
    print(c)
    print("hello")


if __name__ == "__main__":
    main()