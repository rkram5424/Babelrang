angular.module('starter.services', ['ngResource'])

.factory('Babelrang', function($http) {
  var history = [{
    id: "test1",
    text: "The quick brown fox jumps over the lazy dog."
  }, {
    id: "test2",
    text: "How much wood could a woodchuck chuck if a woodchuck could chuck wood?"
  }, {
    id: "test3",
    text: "My milkshakes bring all the boys to the yard."
  }];
  // var defaultDate = {
  //   homeLanguage: "en",
  //   enabledLanguages: [

  //   ]
  // };

  return {
    getHistory: function() {
      return history;
    }
  };
});
