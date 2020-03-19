---
layout: post
title: Why we need Containers
---


1. Brief History
2. Chroot
3. Linux Namespace
4. lean about machines  

In machine learning our goal is to minimize error on unseen future examples.  

Test set contains examples not used for training and represent these unseen future examples.  

## Brief History : Understanding history to better understand containers
In late 1970's , Mainframes were a scarce resource for business due to cost. Gaining access to mainframes gave birth to virtualization or what we call now thin client. The landscape changed with invention of 'chroot', the containerization began. It changes the root dir of a process and child process.


##Chroot
It changes parent root dir. of a process. chroot allows us to create container or limited view of our system.
			Root
bin etc usr var home
				chroot EII spotz
				bin etc usr var home
								Abhishek Amit Ayush

##Linux Namespace  
namespaces allows partition of kernel resources, make sure that one set of processes see only the resources allocated to it while other set of processes sees a different set of resources.

There are six linux namespaces, some people consider Cgroups as seventh namespace. But linux Cgroups limits the ability of process to access a system resource.

namespace limit what you can see , cgroup limit what you can access.

Different types of linux namespaces 

1. user : isolates security related identifier and attributes such as user-ids UIDS and group-ids GUIDs. a process can be pid 1 inside container that maps to pid 10 of actual host machine. user namespace can be nested upto 32 times.
2. 

