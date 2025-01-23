from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)

class MyWorkflow(Workflow):  # Inherits from Workflow base class
    @step  # Decorator marking this as a workflow step
    async def my_step(self, ev: StartEvent) -> StopEvent:  # Async method with type hints
        # do something here
        return StopEvent(result="Hello, world!")


async def main():
    w = MyWorkflow(timeout=10, verbose=True)
    result = await w.run()
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
    from llama_index.utils.workflow import draw_all_possible_flows
    draw_all_possible_flows(MyWorkflow, filename="basic_workflow.html")