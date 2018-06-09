import hypothesis.strategies as st
from hypothesis import given

from aiger import hypothesis as aigh


@given(aigh.Circuits, st.data())
def test_aig_to_aag(circ, data):
    circ2 = circ._to_aag()._to_aig()
    assert circ.inputs == circ2.inputs
    assert circ.outputs == circ2.outputs
    test_input = {f'{i}': data.draw(st.booleans()) for i in circ.inputs}
    assert circ(test_input) == circ2(test_input)
    
