const assert = require('assert');
const selectionSort = require('../selection_sort');

describe('selectionSort', ()=> {
  it('correctly sorts an array', ()=> {
    assert.deepStrictEqual(selectionSort([3, -1, 5, 2]), [-1, 2, 3, 5]);
  });

  it('correctly handles negative arrays', ()=>{
    assert.deepStrictEqual(selectionSort([-1, -8, -10, -20 ,-65, -55, -100,]), [-100,-65,-55,-20,-10,-8,-1])
  })

  it('correcly handles negative and positive arrays', ()=>{
    assert.deepStrictEqual(selectionSort([100, 55, 10, 0, -1, -10, -25]), [-25,-10,-1,0,10,55,100])
  })

  it('can handle an empty array', () => {
    assert.deepStrictEqual(selectionSort([]), [])
  })

  it('can handle a single item array', () =>{
    assert.deepStrictEqual(selectionSort([1]), [1])
  })

  it('can handle repeated items in an array', ()=>{
    assert.deepStrictEqual(selectionSort([9,9,9,9,9,8,8,8,8,7,7,7,0,6,6,6,1]), [0,1,6,6,6,7,7,7,8,8,8,8,9,9,9,9,9])
  })
})
