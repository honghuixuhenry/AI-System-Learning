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