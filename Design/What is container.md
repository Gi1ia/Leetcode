## How containers work
Containers hold the components necessary to run desired software. These components include files, environment variables, dependencies and libraries. The host OS constrains the container's access to physical resources, such as CPU, storage and memory, so a single container cannot consume all of a host's physical resources.

### Container image files
Container image files are complete, static and executable versions of an application or service and differ from one tech to other.
Docker image are made up of multiple layers, which start with a base image. 
The base image includes all of the dependencies needed to execute code in a container. Each image has a readable/writable layer on top of static unchanging layers. 
Because each container has its own specific container layer that customizes that specific container, underlying image layers can be saved and reused in multiple containers. An Open Container Initiative (OCI) image is made up of a manifest, file system layers and configurations. An OCI image has two specifications to operate: a runtime and an image specification. Runtime specifications outline the functioning of a file system bundle, which are files containing all necessary data for performance and runtimes. The image specification contains the information needed to launch an application or service in the OCI container.

## COntainers VS VMs
Containers are different from server virtualization in that a virtualized architecture emulates a hardware system. Each VM can run an OS in an independent environment and present to the application, via abstraction, a substitute to a physical machine. The hypervisor emulates hardware from pooled CPUs, memory, storage and network resources, which can be shared numerous times by multiple instances of VMs.
[VMs take up more space because they need a guest OS to run. Containers don't consume as much space because each container shares the host's OS.](https://cdn.ttgtmedia.com/rms/onlineImages/windows_server-virtual_machines_vs_containers.png)
VMs can require substantial resource overhead, such as memory, disk and network input/output (I/O), because each VM runs an OS, meaning that VMs can be large and take longer to create than containers. Because containers share the OS kernel, only one instance of an OS can run many isolated containers. The OS supporting containers can also be smaller, with fewer features, than an OS for a VM or physical application installation.

### Hypervisor
A hypervisor is a function which abstracts -- isolates -- operating systems and applications from the underlying computer hardware. This abstraction allows the underlying host machine hardware to independently operate one or more virtual machines as guests, allowing multiple guest VMs to effectively share the system's physical compute resources, such as processor cycles, memory space, network bandwidth and so on. A hypervisor is sometimes also called a virtual machine monitor. [(source)](https://searchservervirtualization.techtarget.com/definition/hypervisor)


Credit: [What is container](https://searchitoperations.techtarget.com/definition/container-containerization-or-container-based-virtualization)