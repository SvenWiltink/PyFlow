import unittest
from CodeFlow.workflow import Workflow, State


class TestState(State):

    called = False

    def run(self):
        assert TestState.called is False
        TestState.called = True


class NotAState:

    def run(self):
        pass


class NoRunMethodState(State):
    pass


class TestWorkFlow(unittest.TestCase):

    workflowFile = "tests/resources/workflow.json"

    def createWorkflow(self):
        return Workflow.loadFromFile(self.workflowFile)

    def test_name(self):
        workflow = self.createWorkflow()
        assert workflow.name == 'test'

    def test_run(self):
        workflow = self.createWorkflow()
        workflow.run()
        assert TestState.called is True

    def test_is_not_state(self):
        workflow = Workflow.loadFromFile("tests/resources/not_a_state_workflow.json")
        with self.assertRaises(TypeError):
            workflow.run()

    def test_no_run_method(self):
        workflow = Workflow.loadFromFile("tests/resources/no_run_method_state_workflow.json")
        with self.assertRaisesRegexp(RuntimeError, "run function not implemented"):
            workflow.run()
