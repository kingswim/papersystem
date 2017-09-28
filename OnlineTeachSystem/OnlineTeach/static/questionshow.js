var doSomething = function(err, values) {
    console.log(err, values);
  };

  var schema = {
    options: {
      hideNotReq: true
    },
    title: {
      label: 'Insert Title here', className: 'title'
    },
    submitButton: {
      label: 'Submit', className: 'submit-btn' 
    },
    onSubmit: doSomething,
    body: [
      {label: '1. Question', tag: 'input', type: 'text',
        skip: {
          cond: '=',
          val: 'yes',
          questions: [1, 2]
        }
      },

      {label: '2. Second question', tag: 'textarea', placeholder: 'fill this'},

      {label: '3. Another question', tag: 'radio', 
       data : [ 
        {'value': '1', 'label': 'option 1'},
        {'value': '2', 'label': 'option 2'},
        {'value': '3', 'label': 'option 3'}
       ],
       skip: [
        {val: '1', cond: '=', questions: [0]},
        {val: '2', cond: '=', questions: [1]},
        {val: '3', cond: '=', questions: [4]}
       ]
      },
      {label: '4. You almost finish', tag: 'checkbox', data : [ 
        {'value': '4', 'label': 'option 4'},
        {'value': '5', 'label': 'option 5'},
        {'value': '6', 'label': 'option 6'}
      ]},
      {label: '5. This is the last one', tag: 'textarea'}
    ]
  };

new Survey().create(document.getElementById('main'), schema);
  
