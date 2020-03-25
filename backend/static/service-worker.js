const cacheName = 'cache-v4';
const precacheResources = [
  'assets/css/styles.min.css',
  'assets/fonts/fontawesome5-overrides.min.css',
  // 'assets/js/main.js',
  // 'assets/js/home.js',
  // 'assets/js/script.min.js',
  'assets/img/logo_title.png',
  'assets/img/icons-192.png',
  'assets/img/icons-512.png'
];

self.addEventListener('install', event => {
  console.log('Service worker install event!');
  event.waitUntil(
    caches.open(cacheName)
      .then(cache => {
        return cache.addAll(precacheResources);
      })
  );
});

self.addEventListener('activate', event => {
  console.log('Service worker activate event!');
});

self.addEventListener('fetch', event => {
  // console.log('Fetch intercepted for:', event.request.url);
  event.respondWith(caches.match(event.request)
    .then(cachedResponse => {
        if (cachedResponse) {
          return cachedResponse;
        }
        return fetch(event.request);
      })
    );
});