// Stephen Kalmakis, 7 years prior at Google
// https://www.linkedin.com/pub/stephen-kalmakis/4/9b2/89

// First question asked if I could describe the various position attirubtes (fixed, static, absolute, relative)
// We talked about css:position:sticky for a little bit

function getElementsByClassName(className) { // className = "blue.red"
//   return document.querySelectorAll("." + className);
  var result = [];
  var htmlNode = document.documentElement; // returns HTML node
  recurseNode(htmlNode, result, className);
  return result;
}

function recurseNode(curNode, result, className) {
  if (className.split(" ").indexOf(curNode.className) >= 0) {
    result.append(curNode);
  }
  for (var i=0; i<curNode.children.length; i++) {
    recurseNode(curNode.children[i], result, className);
  }
}
