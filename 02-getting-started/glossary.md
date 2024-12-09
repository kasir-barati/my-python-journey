# Dictionary

<dl>
  <dt id="teletypewritersDefinition">
    <a href="#teletypewritersDefinition">#</a>
    TTY
  </dt>
  <dd>
    Comes from electromechanical teleprinters or 
    <b>t</b>ele<b>ty</b>pewriters.
  </dd>
  <dd>
    <img src="./assets/tty.png" />
  </dd>
  <dd>
    <a href="https://askubuntu.com/a/481915/820307">
    Learn more
  </dd>
  <dt id="memoryCellDefinition">
    <a href="#memoryCellDefinition">#</a>
    Memory cell
  </dt>
  <dd>
    An <a href="https://commons.wikimedia.org/wiki/File:Electronic_circuit.jpg">electronic circuit</a>.
  </dd>
  <dd>Stores one bit of binary information.</dd>
  <dd>
    Stores a logic 1 (high voltage level) and reset to store a logic 0 (low voltage level).
  </dd>
  <dd>
    <img 
      src="./assets/bit-byte-memory-cell.png"
      alt="Each byte is 8 bit, and each memory cell has an address."
    />
  </dd>
  <dt id="fStringsDefinition">
    <a href="#fStringsDefinition">#</a>
    <i>f-strings</i>
  </dt>
  <dd>String literals that have embedded expressions.</dd>
  <dd>
    <pre lang="python">
      <code>
        name = "Fred"
        f"He said his name is {name}."
      </code>
    </pre>
  </dd>
  <dd>
    <a href="https://docs.python.org/3/reference/lexical_analysis.html#f-strings">Learn more here</a>.
  </dd>
  <dt id="arithmeticProgressionsDefinition">
    <a href="#arithmeticProgressionsDefinition">#</a>
    Arithmetic progressions
  </dt>
  <dd>
    A sequence of numbers in which the difference between consecutive terms is constant.
  </dd>
  <dd>
    General formula: <code>a, a+d, a+2d, a+3d, ...</code>
    <br />
    <code>a</code> is the first term.
    <br />
    Fixed difference is called the common difference (represented as <code>d</code>).
  </dd>
  <dd>
    Positive common difference example sequence: <code>3, 7, 11, 15, 19, ...</code>
  </dd>
  <dd>
    Negative common difference example sequence: <code>20, 15, 10, 5, 0, ...</code>
  </dd>
  <dt id="docstringDefinition">
    <a href="#docstringDefinition">#</a>
    docstring
  </dt>
  <dd>Short for documentation string.</dd>
  <dd>
    A special string used to document a module, <code>class</code>, or <code>function</code> in Python.
  </dd>
  <dd>Stored as part of the function’s metadata.</dd>
  <dt id="callByReferenceDefinition">
    <a href="#callByReferenceDefinition">#</a>
    Call by reference
  </dt>
  <dd>
    The value is always an object reference, not the value of the object.
  </dd>
  <dd>
    <pre lang="python">
      <code>
      robot = {}
      def deactivate(p):
          p['active'] = False
      print("Robot before function call: ", robot)
      deactivate(robot)
      print("Robot after function call: ", robot)
      </code>
    </pre>
  </dd>
  <dd><a href="#call-by-value-vs-call-by-reference">Check this to understand it better</a></dd>
  <dt id="callByValueDefinition">
    <a href="#callByValueDefinition">#</a>
    Call by value
  </dt>
  <dd>
    The actual parameters are evaluated and their values are copied to the callee.
  </dd>
  <dd>
    <pre lang="python">
      <code>
      color = 'purple'
      def some_func(p):
          p = 'turquoise'
      print("Before: ", color)
      some_func(color)
      print("After: ", color)
      </code>
    </pre>
  </dd>
  <dd><a href="#call-by-value-vs-call-by-reference">Check this to understand it better</a></dd>
</dl>

## Call by Value VS Call by Reference

![Call by value VS call by reference](./assets/call-by-value-vs-call-by-ref.gif)
