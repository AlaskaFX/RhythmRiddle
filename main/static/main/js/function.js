document.querySelectorAll('.faq details').forEach((item) =&gt; {
  item.addEventListener('toggle', (event) =&gt; {
    if (event.target.open) {
      document.querySelectorAll('.faq details').forEach((otherItem) =&gt; {
        if (otherItem !== event.target) {
          otherItem.removeAttribute('open');
        }
      });
    }
  });
});