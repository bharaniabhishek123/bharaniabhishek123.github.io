---
layout: post
title: Why we need Containers
---


1. Brief History
2. Chroot
3. Linux Namespace
4. lean about machines  


## Brief History : Understanding history to better understand containers
In late 1970's , Mainframes were a scarce resource for business due to cost. Gaining access to mainframes gave birth to virtualization or what we call now thin client. The landscape changed with invention of 'chroot' as the containerization began. It changes the root dir of a process and child process.


##Chroot
It changes parent root dir. of a process. chroot allows us to create container or limited view of our system. 

It changes root, it changes the aparent root of process and it's child process. 
Child process can see limited view of file system.

			Root /
			|
			____________________
			|    |    |   |    |
			bin  etc  usr var  home
								___________________
								|    	 |        |
								chroot 	EII 	spotz
								|	
							____________________
							|    |    |   |    |				
							bin etc  usr var  home

							The root is branched out to chroot, these have no view to rest of the system. chroot dir allows separate other access from group of users.

In 2007, Google announce work with process container. Control group was new name given to containers.
In 2013, LMCTFY was open-sourced. 


##Linux Namespace  
namespaces allows partition of kernel resources, make sure that one set of processes see only the resources allocated to it while other set of processes sees a different set of resources.

There are six linux namespaces, some people consider Cgroups as seventh namespace. But linux Cgroups limits the ability of process to access a system resource.

namespace limit what you can see , cgroup limit what you can access.

Different types of linux namespaces 

1. user : isolates security related identifier and attributes such as user-ids UIDS and group-ids GUIDs. a process can be pid 1 inside container that maps to pid 10 of actual host machine. user namespace can be nested upto 32 times. Keeper user isolated incase of any security breaches.

2. IPC : Inter process conmmunications, this namesoace isolates system resources
allows container to communication with each other.

3. UTS : Isolation of host name for unix containers. Allows us to communicate with container with host name.

4. Mount : It controls the file system mount point.

5. PID : Allows for isolation of process id number. 

6. Network : have a copy of network for each containers.


## Docker

A wrapper around linux container, with powerful set of functions and capabilities. 

1. Portable Deployment Across machine

2. Application Centric

3. Automatic Build

4. Versioning 

5. Component Re-Use

6. Sharing Images

7. Tool Ecosystem

Copy on Write  : COW , every time we want to make change, we first should have a copy of file and then change the file.


### Pods 
Inside the pod each container share the ip address. Applications inside pod have access to shared volume. 


Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 172.31.111.20:6443 --token vcba6z.wd0maymj6bg0thvx \
    --discovery-token-ca-cert-hash sha256:2b79aff82c7b50210830cb7a23128674adf7044b28f8e03c85aaa239bba2ea67 

## sample yaml for kubeclt 

```
apiVersion: v1
kind: Pod
metadata:
    name: examplepod
    namespace: pod-example 
spec:
    volumes:
    - name: html
      emptyDir: {}
    containers:
    - name: webcontainer
      image: nginx
      volumeMounts:
      - name: html
        mountPath: /user/share/nginx/html
    - name: filecontainer
      image: debian
      volumeMounts:
      - name: html 
        mountPath: /html 
      command: ["bin/sh", "-c"]
      args:
         - while true; do
            date >> /html/index.html;
            sleep 1;
        done 
```
