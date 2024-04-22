import docker

# Function to list all Docker containers
def list_containers():
    try:
        # Create a Docker client
        client = docker.from_env()
        
        # Get a list of all containers
        containers = client.containers.list()
        
        print("List of Docker Containers:")
        for container in containers:
            print(f"Container ID: {container.short_id}, Name: {container.name}, Status: {container.status}")
            
    except Exception as e:
        print(f"Error: {e}")

# Function to run a Docker container
def run_container(image, name):
    try:
        # Create a Docker client
        client = docker.from_env()
        
        # Run a new container from the specified image
        container = client.containers.run(image, detach=True, name=name)
        
        print(f"Container {container.short_id} is running.")
        
    except Exception as e:
        print(f"Error: {e}")

# Function to stop a Docker container
def stop_container(container_id):
    try:
        # Create a Docker client
        client = docker.from_env()
        
        # Get the container object
        container = client.containers.get(container_id)
        
        # Stop the container
        container.stop()
        
        print(f"Container {container_id} is stopped.")
        
    except Exception as e:
        print(f"Error: {e}")

# Function to remove a Docker container
def remove_container(container_id):
    try:
        # Create a Docker client
        client = docker.from_env()
        
        # Get the container object
        container = client.containers.get(container_id)
        
        # Remove the container
        container.remove()
        
        print(f"Container {container_id} is removed.")
        
    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    # List all Docker containers
    print("\n")
    print("-" * 20 + " List Containers " + "-" * 20)
    list_containers()
    
    # Run a new Docker container
    print("\n")
    print("-" * 20 + " Run Container " + "-" * 20)
    run_container("nginx", "my_nginx_container")
    
    # List all Docker containers again to see the new one
    print("\n")
    print("-" * 20 + " List Containers " + "-" * 20)
    list_containers()
    
    # Stop the container
    print("\n")
    print("-" * 20 + " Stop Container " + "-" * 20)
    stop_container("my_nginx_container")
    
    # List all Docker containers again to see the updated status
    print("\n")
    print("-" * 20 + " List Containers " + "-" * 20)
    list_containers()
    
    # Remove the container
    print("\n")
    print("-" * 20 + " Remove Container " + "-" * 20)
    remove_container("my_nginx_container")
    
    # List all Docker containers again to confirm removal
    print("\n")
    print("-" * 20 + " List Containers " + "-" * 20)
    list_containers()

if __name__ == "__main__":
    main()
