# *preface*

In late 2014, Kevin Conner formed the Cloud Enablement team at Red Hat to adapt the company's middleware products for the emerging OpenShift Container Platform, which was built on Kubernetes. Marko Lukša was one of the first engineers to join the team. At that time, Kubernetes was still in its infancy. Version 1.0 had not yet been released, and almost no one had heard of it. Today, Kubernetes is one of the most widely adopted platforms for running applications, both in the cloud and on premises.

 In his first month working with Kubernetes, Marko wrote a two-part blog post about several problems the team encountered when running a JBoss WildFly cluster on Open-Shift and Kubernetes. That post caught the attention of Manning Publications, leading to an invitation to write a book. After years of effort, *Kubernetes in Action* was published in 2017 to widespread acclaim, for which Marko remains deeply grateful.

 With years of rapid evolution in the Kubernetes ecosystem, a second edition became essential. This time, Marko and Kevin have teamed up as co-authors, drawing on their shared experience. The book's scope has grown alongside Kubernetes itself, so *Kubernetes in Action, Second Edition* focuses on the fundamentals of developing applications for and on Kubernetes.

 The authors hope this book will help you harness Kubernetes effectively and enjoy the journey.

# *acknowledgments*

We would like to thank the team at Manning Publications for giving us the opportunity to write this book. We're especially thankful to our development editor, Elesha Hyde, who remained incredibly patient and endlessly supportive, even when we were missing our deadlines.

 We would also like to thank Raphael Villela, who, together with Elesha, was among the first to read and comment on the chapters as they were written. They identified areas that lacked clarity and could have confused readers. Their feedback helped improve the text tremendously.

 We would like to thank our technical proofreaders, Mayur Patil and Werner Dijkerman, and all our external reviewers: Alain Lompo, Alex Speranza, Anand Edward, Andres Sacco, Aron Trauring, Björn Neuhaus, Borko Djurkovic, Charles Henrique Gonçalves Santos, Conor Redmond, Fernando Bugni, Gandhi Rajan, Glen Yu, Gunnar Prüfer, Jared Duncan, Jaume Lopez, Jay Vyas, Joan Fuster, John Guthrie, Jorge Contreras, Kent Spillner, Marlon Briguera, Neil Croll, Rob Pacheco, Roman Levchenko, Ruben Vandeginste, Ryan Burrows, Satadru Roy, Sébastien Portebois, Stefano Ongarello, Tylor Dolezal, and Vittal Damaraju, who caught errors and omissions that slipped through the earlier reviews. Their careful attention to detail helped make this book more accurate and reliable.

 We would also like to thank the readers who purchased the early version of the book through Manning's MEAP program and shared their feedback in the online forum or reached out directly. Your comments and suggestions were invaluable in helping to refine and improve the final version of this book.

 Lastly, we thank our families, whose patience and understanding sustained us through the many hours spent on this project instead of with them.

Thank you all!

# *about this book*

*Kubernetes in Action, Second Edition* provides the foundation for developing and running applications on Kubernetes efficiently. It focuses on the development side building, configuring, deploying, and managing apps—rather than operating production clusters.

 The book starts with container basics (using Docker or Podman) for beginners, then guides the reader step by step through core and advanced Kubernetes concepts in a logical progression. Whether you're new to Kubernetes or already have some experience, you'll gain practical, hands-on understanding of how to use the platform effectively for real application development.

### *Who should read this book*

*Kubernetes in Action, Second Edition* is primarily for application developers and system administrators who want to build, containerize, and run applications on Kubernetes. The book is suitable for both beginners and experienced engineers—no prior knowledge of containers or Kubernetes is required.

 The concepts are introduced progressively, from the basics onward through straightforward examples that don't assume deep expertise. Readers should have a basic understanding of programming, computer networking, Linux command-line usage, and common protocols such as HTTP.

### *How this book is organized: A road map*

The book is divided into five parts that cover 18 chapters. Part 1 introduces Kubernetes and the container technologies it builds on:

- Chapter 1 gives a high-level overview of Kubernetes—what it is, the problems it solves, how it transforms application deployment and operations, and whether it's the right choice for you and your organization.
- Chapter 2 covers container fundamentals—how containers differ from virtual machines, the underlying technologies, building your first container image, and running it with Docker or Podman.
- Chapter 3 takes that container image and runs it in Kubernetes (locally or in the cloud), shows how to expose the application externally, and demonstrates simple horizontal scaling.
- Chapter 4 explores the Kubernetes API and basic object types such as Node and Event to understand how Kubernetes represents and manages cluster state.

Part 2 dives into the core concepts for running, organizing, and keeping applications healthy:

- Chapter 5 introduces pods—the fundamental building block—including how applications run in containers inside pods and how sidecar/helper containers enhance functionality.
- Chapter 6 covers the pod life cycle—startup/shutdown actions, liveness/readiness/startup probes, and keeping containers healthy.
- Chapter 7 explains how to organize large numbers of pods and other objects using labels, namespaces, and related mechanisms for clarity and maintainability.

Part 3 focuses on configuring applications and attaching storage via the Kubernetes API:

- Chapter 8 shows how to pass configuration through command-line arguments, environment variables, ConfigMaps (for nonsensitive data), and Secrets (for sensitive values such as keys, tokens, and passwords).
- Chapter 9 covers adding volumes to pods, mounting them into containers, persisting data across restarts, sharing files between containers, node filesystem access, and injecting data from ConfigMaps, Secrets, or Pod metadata.
- Chapter 10 introduces persistent storage with PersistentVolumes (PV) and PersistentVolumeClaims (PVC), static versus dynamic provisioning, node-local vs. network storage, ephemeral vs. long-lived volumes, and volume snapshots.

Part 4 explains intracluster and external communication:

- Chapter 11 covers pod-to-pod communication, using Services to provide stable endpoints for groups of pods, service discovery, external exposure, and readiness signaling.
- Chapter 12 describes exposing multiple Services externally via a single public IP using Ingress.

 Chapter 13 introduces the Gateway API as a modern alternative to Ingress, covering resources such as Gateway, HTTPRoute, TLSRoute, TCPRoute, UDPRoute, and others for internal and external traffic.

Part 5 focuses on higher-level controllers for managing diverse workloads (you rarely create pods directly):

- Chapter 14 explains ReplicaSets and how they maintain a desired number of pod replicas for high availability.
- Chapter 15 covers Deployments, which manage ReplicaSets automatically and enable controlled rollouts, rollbacks, and updates.
- Chapter 16 introduces StatefulSets for stateful applications, providing stable network identities, ordered scaling, and other stateful behaviors.
- Chapter 17 describes DaemonSets, which create and manage one pod per node for node-level agents, monitoring, and so forth.
- Chapter 18 concludes the book by explaining batch processing in Kubernetes. You'll learn how to run one-off jobs using a Job object or schedule recurring tasks at specific times using a CronJob.

Readers who are new to containers or Kubernetes and those who want a solid, step-bystep understanding should read the chapters in sequence from beginning to end. Each chapter builds directly on the concepts and examples introduced in the previous ones, so following the order ensures you have the necessary foundation before moving forward.

 Readers who already have working experience with Kubernetes and are using the book more as a reference or deep-dive resource can jump to specific chapters that address their current needs or interests.

#### *About the code*

While this book doesn't contain a lot of actual source code, it does contain a lot of manifests of Kubernetes resources in YAML format and shell commands along with their outputs. These are formatted in a fixed-width font like this to separate them from ordinary text.

 Shell commands are mostly in **bold** to clearly separate them from their output, but sometimes only the most important parts of the command or parts of the command's output are in bold for emphasis. In most cases, the command output has been reformatted to make it fit into the limited space in the book. Also, because the Kubernetes CLI tool kubectl is constantly evolving, newer versions may print out more information than what's shown in the book, so don't be confused if they don't match exactly.

 Listings sometimes include a line-continuation marker (➥) to show that a line of text wraps to the next line. They also include annotations, which highlight and explain the most important parts.

 All the samples in the book have been tested with Kubernetes version 1.35 running in Google Container Engine and in a local cluster run with kind. The complete source code and YAML manifests can be downloaded from the publisher's website at [www.manning.com/books/kubernetes-in-action-second-edition](http://www.manning.com/books/kubernetes-in-action-second-edition).

#### *liveBook discussion forum*

Purchase of *Kubernetes in Action, Second Edition* includes free access to liveBook, Manning's online reading platform. Using liveBook's exclusive discussion features, you can attach comments to the book globally or to specific sections or paragraphs. It's a snap to make notes for yourself, ask and answer technical questions, and receive help from the author and other users. To access the forum, go to [https://livebook.man](https://livebook.manning.com/book/kubernetes-in-action-second-edition/discussion)[ning.com/book/kubernetes-in-action-second-edition/discussion.](https://livebook.manning.com/book/kubernetes-in-action-second-edition/discussion)

 Manning's commitment to our readers is to provide a venue where a meaningful dialogue between individual readers and between readers and the author can take place. It is not a commitment to any specific amount of participation on the part of the author, whose contribution to the forum remains voluntary (and unpaid). We suggest you try asking the authors some challenging questions lest their interest stray! The forum and the archives of previous discussions will be accessible from the publisher's website as long as the book is in print.

#### *Other online resources*

You can find a wide range of additional Kubernetes resources at the following locations:

- The Kubernetes website (<https://kubernetes.io>)
- The Kubernetes Blog, which regularly posts interesting info ([http://blog](http://blog.kubernetes.io/) [.kubernetes.io\)](http://blog.kubernetes.io/)
- The Kubernetes Community's Slack channel [\(http://slack.k8s.io](http://slack.k8s.io/))
- The Kubernetes YouTube channel [\(https://www.youtube.com/channel/](https://www.youtube.com/channel/UCZ2bu0qutTOM0tHYa_jkIwg) [UCZ2bu0qutTOM0tHYa\\_jkIwg\)](https://www.youtube.com/channel/UCZ2bu0qutTOM0tHYa_jkIwg)

Since Kubernetes is open source, there's a wealth of information available in the Kubernetes source code itself. You'll find it at <https://github.com/kubernetes/kubernetes> and related repositories.

# *about the authors*

![](_page_7_Picture_1.jpeg)

**MARKO LUKŠA** is a software engineer with over 40 years of programming experience. He wrote his first program in 1985 at the age of six and has worked professionally in software development since his teenage years. His projects range from early dynamic websites to large-scale ERP systems, frameworks, and middleware.

 After studying computer science and working for a few local software companies, he joined Red Hat, where he contributed to numerous projects, including CDI/Weld, Infinispan/JBoss Data Grid, and an alternative open source implementation of

the Google App Engine APIs.

 He has worked with Kubernetes since late 2014, starting with Red Hat's Cloud Enablement team to help the company's middleware fully use Kubernetes and Open-Shift. He later joined the OpenShift Service Mesh team, where his work on Istio deepened his insight into Kubernetes' advanced networking and service management features.

 In 2025, he stepped away from Red Hat to complete this book and is currently an independent software engineer.

![](_page_8_Picture_2.jpeg)

**KEVIN CONNER** is a senior engineering leader with over 30 years of software development experience and more than 17 years of building and managing global engineering teams. He specializes in distributed systems, cloud technologies, and Kubernetes. His career began in the early 1990s as a kernel developer working on network and SCSI drivers for fault-tolerant telecommunications systems, progressed through enterprise Java development at Sun Microsystems and various financial institutions, and led transaction management systems development at Arjuna Tech-

nologies, where he contributed to OASIS WS-CAF specifications.

 In 2005, JBoss acquired Arjuna Technologies' Transaction Management team along with Kevin. When Red Hat subsequently acquired JBoss, Kevin spent 16 years with the company, progressing from Core Developer to Senior Engineering Manager. He participated in standards work including the W3C WS-Addressing Working Group, served as Chair of the SPEC SOA performance Committee, and was a member of the JCP JSR-352 Specification Committee. He created and led the Cloud Enablement team that brought Red Hat's middleware products to OpenShift and Kubernetes, established the Istio team, drove the creation of Red Hat OpenShift Service Mesh, and served on the Istio Steering Committee.

 After leaving Red Hat in 2021, Kevin served as Vice President of Engineering at Aviatrix Canada, building teams from the ground up and growing his organization from 16 to 39 engineers. He returned to Red Hat as a consultant in 2022 to work on software supply chain security, contributing to OpenSSF projects including GUAC and working with the CycloneDX community. At Getup Cloud as Chief Engineer, he led security solutions for Kubernetes environments, including the Zora project and Zero CVE solution, while representing the company at KubeCon and participating in the Kubernetes community.

 Kevin rejoined Red Hat in 2025 as a Senior Principal Software Engineer on the Trusted Artifact Signer team, where he focuses on productizing upstream Sigstore projects, model validation for AI/ML workloads, and implementing support for postquantum cryptographic algorithms within Sigstore. He actively participates in the Kubernetes community through conference presentations and contributions to open source projects.

# *about the cover illustration*

The figure on the cover of *Kubernetes in Action, Second Edition* is a "Member of the Divan," the Turkish Council of State or governing body. The illustration is taken from a collection of costumes of the Ottoman Empire published on January 1, 1802, by William Miller of Old Bond Street, London.

 In those days, it was easy to identify where people lived and what their trade or station in life was just by their dress. Manning celebrates the inventiveness and initiative of the computer business with book covers based on the rich diversity of regional culture centuries ago, brought back to life by pictures from collections such as this one.