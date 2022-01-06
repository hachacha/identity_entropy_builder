return (function eval_list(path, method) {
  // alert(arguments[0]);
  function getOffset(el) {
    const rect = el.getBoundingClientRect();
    return {
      left: rect.left + window.scrollX,
      top: rect.top + window.scrollY
    };
  }

  rand_elem = Math.floor(Math.random() * (25 - 1 + 1) + 1);
  selected_elem = document.getElementsByClassName('md-list-block')[rand_elem];
  window.scrollTo(0, getOffset(selected_elem).top-50);
  link = selected_elem.getElementsByClassName('image-link-wrapper')[0].getElementsByTagName('a')[0].href
  return link;
  

})(arguments[0]);