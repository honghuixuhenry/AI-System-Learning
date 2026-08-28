                         Client
                            │
                            ▼
                        FastAPI
                            │
                  Authentication
                            │
                            ▼
                      Rate Limiter
                            │
                            ▼
                    Request Validation
                            │
                            ▼
                      Bounded Queue
                            │
                            ▼
                       Scheduler
                            │
                            ▼
                     Worker / Async
                            │
                            ▼
                       LLM Service
                      /     |      \
                     /      |       \
                 Cache    Retry    Logging
                           │
                    Circuit Breaker
                           │
                           ▼
                      LLM Interface
                           │
                ┌──────────┼──────────┐
                ▼          ▼          ▼
              Qwen       Llama     DeepSeek

Server works
+
I know how well it works
+
I know when it fails
+
I can locate where it fails