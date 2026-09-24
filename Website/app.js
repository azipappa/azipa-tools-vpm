const copyButton = document.getElementById('copy-url');
const listingUrl = document.getElementById('listing-url');

copyButton?.addEventListener('click', async () => {
  await navigator.clipboard.writeText(listingUrl.textContent.trim());
  const previousLabel = copyButton.textContent;
  copyButton.textContent = 'Copied';
  setTimeout(() => {
    copyButton.textContent = previousLabel;
  }, 1200);
});
