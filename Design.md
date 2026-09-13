System and logic overview

Our program operates as a client-side web extension that functions as an interception layer between the web UI of the commercial banking portal, in this case, between BanBajio and the core banking endpoints like the Nessie API. 
The architecture consists of four primary software modules: the DOM Data Capture Engine, the Heuristic Evaluation Module, the Step-Up Authentication Engine, and the Audit Ledger Subsystem.

When an operator triggers a transaction form submission, the DOM Data Capture Engine intercepts the raw payload prior to network transmission, extracting metadata such as origin account, beneficiary entity, transaction amount, timestamp, and destination category. 
This payload is passed synchronously to the Heuristic Evaluation Module. Depending on the computed threat level, the Step-Up Authentication Engine conditionally interrupts the execution flow, either enforcing 2FA/biometric verification or diverting the transaction into a temporary 24-hour preventive escrow holding state within the banking core. All evaluation outcomes, parameter vectors, and operator decision trails are logged locally and transmitted to the Audit Ledger Subsystem.

Algorithmic Logic & Risk Scoring Engine operations:

The core evaluation mechanism utilizes a weighted additive threat model that computes a composite numerical score ranging from 0 to 100 for each incoming transaction payload. 
The pipeline initializes every transfer at a baseline score of +10. It then processes the payload through five deterministic constraint filters: maximum amount limits, high-risk destination categories (such as crypto exchanges or offshore trusts), curfew time windows (typically 01:00 AM to 05:00 AM), and velocity burst detection.
The velocity filter evaluates a trailing 60-second sliding window of previous execution timestamps to detect automated high-frequency bot behavior.

The evaluation pipeline routes execution through three deterministic action thresholds based on the final computed risk score:

Low risk, under 50. The transaction bypasses additional verification. The network request proceeds directly to the core banking SPEI settlement API, and the event is written to the audit log as approved.
Medium risk between 50-75. The runtime halts the outgoing API request and mounts a Step-Up Authentication modal. The user must successfully pass dynamic 4-character token validation or biometric identification before the network request is released.
High Risk, over 75. The request execution is completely intercepted. The system restricts immediate execution, prompting an administrative review that forces the funds into an Escrow Holding state, requires multi-signatory authorization, or cancels the payload outright.

