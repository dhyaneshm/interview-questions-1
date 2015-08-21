/* 
Build a simple templating function that will render a substituted string given some template markup and a params object
*/
var template = {};

var markup = "hello {{name}} {{#if awake}} this is cool {{/if}}!";
var params = {name:"Seth", awake:false};

function substitute(key, params) {
  if (key in params){
    var value = params[key];
    return value;
  }
  return "";
}

var ENDIF = "{{/if}}"; 
template.render = function(markup, params) {
  while (markup.indexOf("{{") >= 0) {
    var start = markup.indexOf("{{");
    var end = markup.indexOf("}}");
    var enclosed = markup.substring(start+2, end);
    if (enclosed.substring(0,3) === '#if'){
      //find endif
      var endIf = markup.indexOf(ENDIF);
      var flag = enclosed.substring(3).trim();
      if (flag in params && params[flag]){
        //remove the if blocks
        markup = markup.replace(markup.substring(start, endIf+ENDIF.length), markup.substring(end+2, endIf));
      } else {
        //remove the if blocks and the content inside them
        markup = markup.replace(markup.substring(start, endIf+ENDIF.length), "");
      }
    } else {
      var substitutedContent = substitute(markup.substring(start+2, end), params);
      markup = markup.replace(markup.substring(start, end+2), substitutedContent);
    }
  }
  return markup;
}

console.log(template.render(markup, params));
