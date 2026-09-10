# Pre-curated, high-quality learning content and quizzes for all 10 topics.
# Used directly when GEMINI_API_KEY is not configured, or as an instant offline fallback.

CURATED_TOPIC_DATA = {
    "Python Basics": {
        "summary": "Python is a high-level, interpreted programming language known for its clear syntax and code readability. It supports multiple paradigms including procedural, object-oriented, and functional programming, making it ideal for beginners and professionals alike.",
        "key_points": [
            "Dynamically typed: Variable types are checked at runtime.",
            "Automatic memory management via garbage collection and reference counting.",
            "Indentation-driven syntax eliminates the need for curly braces."
        ],
        "questions": [
            {
                "id": 1,
                "question": "Which of the following is an immutable data type in Python?",
                "options": ["List", "Dictionary", "Tuple", "Set"],
                "correct_index": 2,
                "explanation": "Tuples cannot be modified after creation, making them immutable. Lists, dictionaries, and sets are mutable."
            },
            {
                "id": 2,
                "question": "What is the output of bool('False') in Python?",
                "options": ["False", "True", "None", "ValueError"],
                "correct_index": 1,
                "explanation": "Any non-empty string in Python evaluates to True in a boolean context, regardless of its textual content."
            },
            {
                "id": 3,
                "question": "Which keyword is used to define an anonymous (inline) function?",
                "options": ["def", "func", "lambda", "inline"],
                "correct_index": 2,
                "explanation": "The 'lambda' keyword creates small anonymous functions without a standard def statement."
            }
        ]
    },
    "Machine Learning": {
        "summary": "Machine Learning (ML) focuses on building systems that learn patterns from data and improve their performance through experience rather than explicit programming. Core categories include supervised, unsupervised, and reinforcement learning.",
        "key_points": [
            "Supervised Learning trains on labeled inputs and ground truth targets.",
            "Unsupervised Learning discovers hidden structure (like clusters) in unlabeled data.",
            "Overfitting occurs when a model memorizes training noise instead of generalizing."
        ],
        "questions": [
            {
                "id": 1,
                "question": "Which metric is most appropriate for evaluating a classifier on a heavily imbalanced dataset?",
                "options": ["Accuracy", "F1-Score / PR AUC", "Mean Squared Error", "R-squared"],
                "correct_index": 1,
                "explanation": "Accuracy is misleading when classes are imbalanced (e.g. 99% majority class). Precision, Recall, and F1-score provide an objective evaluation."
            },
            {
                "id": 2,
                "question": "What is the primary role of regularization techniques like L1 (Lasso) and L2 (Ridge)?",
                "options": ["Increase training speed", "Prevent overfitting", "Handle missing values", "Normalize input features"],
                "correct_index": 1,
                "explanation": "Regularization penalizes large weights in the loss function, reducing model complexity and curbing overfitting."
            },
            {
                "id": 3,
                "question": "Which algorithm is commonly used for unsupervised clustering?",
                "options": ["Linear Regression", "K-Means", "Logistic Regression", "Random Forest Classifier"],
                "correct_index": 1,
                "explanation": "K-Means partitions unlabelled observations into K distinct clusters based on feature proximity to cluster centroids."
            }
        ]
    },
    "Data Structures": {
        "summary": "Data structures provide organized formats for storing, managing, and accessing data efficiently. Choosing the right data structure directly determines algorithmic time and space complexity.",
        "key_points": [
            "Arrays provide O(1) random access by index but O(n) insertions/deletions.",
            "Hash tables offer average O(1) lookups, insertions, and deletions.",
            "Binary Search Trees maintain ordered elements with average O(log n) operations."
        ],
        "questions": [
            {
                "id": 1,
                "question": "What is the average time complexity for searching an element in a balanced Binary Search Tree (BST)?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
                "correct_index": 2,
                "explanation": "Each comparison in a balanced BST cuts the remaining search space in half, yielding O(log n) time."
            },
            {
                "id": 2,
                "question": "Which data structure follows the Last-In, First-Out (LIFO) principle?",
                "options": ["Queue", "Stack", "Linked List", "Heap"],
                "correct_index": 1,
                "explanation": "A Stack operates on LIFO (e.g., call stack, undo history), whereas a Queue operates on FIFO."
            },
            {
                "id": 3,
                "question": "Which data structure is typically used to implement Breadth-First Search (BFS) in a graph?",
                "options": ["Stack", "Queue", "Priority Queue", "Disjoint Set"],
                "correct_index": 1,
                "explanation": "BFS explores nodes level-by-level using a FIFO Queue to track unvisited adjacent nodes."
            }
        ]
    },
    "Computer Networks": {
        "summary": "Computer networks interconnect computing devices to share resources and exchange packets. Network models like OSI (7 layers) and TCP/IP (4 layers) standardize communication protocols.",
        "key_points": [
            "TCP is connection-oriented, reliable, and provides flow/congestion control.",
            "UDP is connectionless and low-latency, commonly used for streaming and gaming.",
            "DNS translates human-readable hostnames to numerical IP addresses."
        ],
        "questions": [
            {
                "id": 1,
                "question": "At which OSI layer does the IP (Internet Protocol) operate?",
                "options": ["Transport Layer", "Network Layer", "Data Link Layer", "Application Layer"],
                "correct_index": 1,
                "explanation": "The Network layer (Layer 3) handles logical addressing and packet routing across networks."
            },
            {
                "id": 2,
                "question": "What type of handshake does TCP use to establish a reliable connection?",
                "options": ["Two-way handshake", "Three-way handshake (SYN, SYN-ACK, ACK)", "Four-way handshake", "Token exchange"],
                "correct_index": 1,
                "explanation": "TCP establishes connections through SYN -> SYN-ACK -> ACK before data transmission begins."
            },
            {
                "id": 3,
                "question": "Which protocol securely maps domain names (e.g. google.com) to IP addresses?",
                "options": ["DHCP", "DNS / DNSSEC", "SNMP", "ARP"],
                "correct_index": 1,
                "explanation": "Domain Name System (DNS) performs name resolution; DNSSEC adds cryptographic authentication."
            }
        ]
    },
    "Operating Systems": {
        "summary": "An Operating System manages computer hardware and software resources, providing common services and abstractions like processes, threads, virtual memory, and file systems.",
        "key_points": [
            "Processes represent isolated program instances with private memory spaces.",
            "Threads share the memory space of their parent process for lightweight concurrency.",
            "Virtual memory uses paging to give processes the illusion of contiguous, dedicated RAM."
        ],
        "questions": [
            {
                "id": 1,
                "question": "Which condition is NOT one of the four Coffman conditions necessary for deadlock?",
                "options": ["Mutual Exclusion", "Hold and Wait", "Preemption allowed", "Circular Wait"],
                "correct_index": 2,
                "explanation": "The four deadlock conditions are Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. If preemption is allowed, deadlock is avoided."
            },
            {
                "id": 2,
                "question": "What is a 'context switch' in an operating system?",
                "options": ["Switching network protocols", "Saving and restoring CPU state between processes", "Writing memory to swap disk", "Recompiling running code"],
                "correct_index": 1,
                "explanation": "A context switch stores the state (registers, program counter) of an active process and restores another to allow multitasking."
            },
            {
                "id": 3,
                "question": "What is the primary benefit of virtual memory paging?",
                "options": ["Increases CPU clock speed", "Enables memory isolation and using disk as auxiliary RAM", "Prevents all software bugs", "Guarantees zero latency access"],
                "correct_index": 1,
                "explanation": "Virtual memory gives each process an isolated address space and allows non-contiguous physical RAM allocations with disk paging."
            }
        ]
    },
    "Database Management Systems": {
        "summary": "A DBMS provides systematic management, storage, querying, and updating of structured and unstructured data. Relational databases enforce ACID guarantees using SQL.",
        "key_points": [
            "ACID: Atomicity, Consistency, Isolation, and Durability guarantee transaction safety.",
            "Normalization reduces data redundancy and prevents update anomalies.",
            "Indexes (e.g., B-Trees) accelerate query performance at the cost of write overhead."
        ],
        "questions": [
            {
                "id": 1,
                "question": "What does the 'I' in ACID transaction properties stand for?",
                "options": ["Integrity", "Isolation", "Immutability", "Indexing"],
                "correct_index": 1,
                "explanation": "Isolation ensures that concurrent transactions execute without interfering with one another's intermediate states."
            },
            {
                "id": 2,
                "question": "Which SQL command is used to remove all records from a table without deleting the table structure, typically faster than DELETE?",
                "options": ["DROP TABLE", "TRUNCATE TABLE", "ALTER TABLE", "PURGE"],
                "correct_index": 1,
                "explanation": "TRUNCATE removes all rows by deallocating pages and does not log individual row deletions, making it much faster than DELETE."
            },
            {
                "id": 3,
                "question": "What is the purpose of a Foreign Key constraint?",
                "options": ["Enforce referential integrity between tables", "Encrypt sensitive columns", "Speed up full-text search", "Auto-generate primary keys"],
                "correct_index": 0,
                "explanation": "A Foreign Key ensures referential integrity by verifying that values match an existing primary key in the referenced parent table."
            }
        ]
    },
    "Artificial Intelligence": {
        "summary": "Artificial Intelligence involves designing computational agents capable of reasoning, perception, knowledge representation, problem solving, and autonomous decision-making.",
        "key_points": [
            "Heuristic search algorithms like A* find optimal paths using cost estimates.",
            "Knowledge graphs model interconnected semantic relationships between entities.",
            "Large Language Models leverage self-attention mechanisms to process sequential tokens."
        ],
        "questions": [
            {
                "id": 1,
                "question": "What core mechanism enables Transformer neural networks to capture long-range token relationships?",
                "options": ["Recurrent feedback loops", "Self-Attention", "Max pooling", "Markov Decision Processes"],
                "correct_index": 1,
                "explanation": "Self-attention computes dynamic weights between all pairs of tokens in a sequence simultaneously, avoiding sequential bottlenecking."
            },
            {
                "id": 2,
                "question": "In search algorithms, what property makes a heuristic 'admissible' for A* search?",
                "options": ["It never underestimates the true cost to the goal", "It never overestimates the true cost to the goal", "It computes in O(1) time", "It returns non-zero values"],
                "correct_index": 1,
                "explanation": "An admissible heuristic never overestimates the actual cost to reach the goal, guaranteeing that A* finds the optimal solution."
            },
            {
                "id": 3,
                "question": "What is the primary role of the Discriminator in a Generative Adversarial Network (GAN)?",
                "options": ["Generate synthetic data", "Distinguish real samples from generator-created fakes", "Optimize learning rate schedules", "Perform dimensionality reduction"],
                "correct_index": 1,
                "explanation": "The Discriminator acts as a binary classifier evaluating whether an incoming sample is from the real training set or synthesized by the Generator."
            }
        ]
    },
    "Java Programming": {
        "summary": "Java is a class-based, object-oriented, strongly-typed language built on the principle of 'Write Once, Run Anywhere' via the Java Virtual Machine (JVM) and bytecode compilation.",
        "key_points": [
            "JVM executes compiled .class bytecode and manages memory via garbage collection.",
            "Object-Oriented principles: Encapsulation, Inheritance, Polymorphism, and Abstraction.",
            "Checked exceptions require explicit handling (try-catch or throws declaration)."
        ],
        "questions": [
            {
                "id": 1,
                "question": "Which keyword prevents a Java class from being subclassed (inherited)?",
                "options": ["static", "abstract", "final", "sealed"],
                "correct_index": 2,
                "explanation": "Marking a class as 'final' prevents other classes from extending it (e.g., java.lang.String is final)."
            },
            {
                "id": 2,
                "question": "What is the difference between String and StringBuilder in Java?",
                "options": ["String is mutable; StringBuilder is immutable", "String is immutable; StringBuilder is mutable", "String cannot be used in multithreading", "There is no difference"],
                "correct_index": 1,
                "explanation": "String objects are immutable; modifying them creates new instances. StringBuilder allows in-place modifications without overhead."
            },
            {
                "id": 3,
                "question": "Which collection implementation in Java maintains elements in sorted order based on their natural comparison or a Comparator?",
                "options": ["HashSet", "ArrayList", "TreeSet", "LinkedList"],
                "correct_index": 2,
                "explanation": "TreeSet is backed by a Red-Black tree and keeps elements sorted in ascending order."
            }
        ]
    },
    "Web Development": {
        "summary": "Modern web development encompasses frontend interfaces (HTML5, modern CSS, JavaScript/TypeScript) and backend services (APIs, databases, server environments) delivering interactive user experiences.",
        "key_points": [
            "DOM (Document Object Model) represents page structure as a tree of inspectable objects.",
            "RESTful APIs communicate over HTTP methods (GET, POST, PUT, DELETE).",
            "Responsive Web Design uses CSS Flexbox, Grid, and media queries to adapt to screen sizes."
        ],
        "questions": [
            {
                "id": 1,
                "question": "Which HTTP status code signifies that a client request succeeded and a new resource was created?",
                "options": ["200 OK", "201 Created", "204 No Content", "301 Moved Permanently"],
                "correct_index": 1,
                "explanation": "HTTP 201 Created indicates the request succeeded and resulted in the creation of one or more new resources."
            },
            {
                "id": 2,
                "question": "What is the purpose of the CORS (Cross-Origin Resource Sharing) mechanism?",
                "options": ["Speed up CSS rendering", "Allow servers to specify which external origins can access their resources", "Compress HTTP payloads", "Encrypt cookie headers"],
                "correct_index": 1,
                "explanation": "CORS is a browser security standard allowing servers to declare which external domains are permitted to load and interact with their API resources."
            },
            {
                "id": 3,
                "question": "Which JavaScript feature allows asynchronous non-blocking code execution with cleaner syntax than nested callbacks?",
                "options": ["Event Bubbling", "Promises / async-await", "Web Workers", "Prototypes"],
                "correct_index": 1,
                "explanation": "async/await built on Promises allows developers to write asynchronous code in a linear, readable, synchronous-looking style."
            }
        ]
    },
    "Cyber Security": {
        "summary": "Cyber security involves protecting computers, networks, programs, and data from unauthorized access, attacks, damage, or exploitation through defense-in-depth strategies.",
        "key_points": [
            "CIA Triad: Confidentiality, Integrity, and Availability form the core of information security.",
            "Public Key Cryptography (asymmetric) uses distinct public and private keys.",
            "Zero Trust Architecture assumes breach and continuously verifies every access request."
        ],
        "questions": [
            {
                "id": 1,
                "question": "Which security vulnerability allows attackers to execute malicious scripts in the browser of another user?",
                "options": ["SQL Injection", "Cross-Site Scripting (XSS)", "Buffer Overflow", "Denial of Service (DoS)"],
                "correct_index": 1,
                "explanation": "XSS occurs when an application includes untrusted user input in web pages without adequate sanitization, allowing client-side script execution."
            },
            {
                "id": 2,
                "question": "What is the fundamental difference between symmetric and asymmetric encryption?",
                "options": ["Symmetric uses two keys; Asymmetric uses one key", "Symmetric uses the same key for encryption & decryption; Asymmetric uses a public-private key pair", "Symmetric is only used for hashing", "Asymmetric cannot encrypt data"],
                "correct_index": 1,
                "explanation": "Symmetric encryption uses a single shared secret key (e.g., AES), while asymmetric encryption uses a mathematically paired public and private key (e.g., RSA)."
            },
            {
                "id": 3,
                "question": "Which defense is most effective against SQL Injection attacks?",
                "options": ["Client-side regex validation only", "Parameterized queries (prepared statements)", "Running the database as root", "Hiding the database schema"],
                "correct_index": 1,
                "explanation": "Parameterized queries ensure user input is treated strictly as data parameters rather than executable SQL syntax."
            }
        ]
    }
}
