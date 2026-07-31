// ----------------- version and caches -----------------



const VERSION = 'v3';

const cachesNames = {
    static: `static-${VERSION}`,
    dynamic: `dynamic-${VERSION}`
}



// ----------------- install -----------------



self.addEventListener('install', event => event.waitUntil(installServiceWorker()));

async function installServiceWorker() {

    // log("Service Worker installation started ");

    const cache = await caches.open(cachesNames["static"]);

    await cache.addAll([
        '/',
        'fallback.html',
        'assets/js/bootstrap.bundle.min.js',
        'assets-2/js/apps.js',
        'assets/js/video.js',
        'assets/css/bootstrap.rtl.min.css',
        'scripts/css/base.css',
        'assets/css/index.css',
        'assets/css/video.css',
        'assets/img/lazy-img.webp',
        "assets/img/hero-bg.webp",
        "assets/img/editor.webp",
        "assets/img/logo.webp",
        "assets/img/logo-footer.webp"
    ]);

    return self.skipWaiting();
}



// ----------------- activate -----------------



self.addEventListener('activate', () => activateSW());

async function activateSW() {

    // log('Service Worker activated');

    const cacheKeys = await caches.keys();
    const cacheValues = Object.values(cachesNames);

    cacheKeys.forEach(cacheKey => {
        if (!cacheValues.includes(cacheKey)) {
            caches.delete(cacheKey);
        }
    });

    return self.clients.claim();
}



// ----------------- fetch -----------------



self.addEventListener('fetch', event => event.respondWith(cacheThenNetwork(event)));

async function cacheThenNetwork(event) {
    const staticCache = await caches.open(cachesNames["static"]);
    const dynamicCache = await caches.open(cachesNames["dynamic"]);

    let cachedResponse = await staticCache.match(event.request).then(res => {
        if (res) {
            // log('Serving From Cache: ' + event.request.url);
            return res;
        }
        return null;
    });

    if (!cachedResponse) {
        cachedResponse = await dynamicCache.match(event.request).then(res => {
            if (res) {
                // log('Serving From Cache: ' + event.request.url);
                return res;
            }
            return null;
        });
    }

    if (cachedResponse) {
        // log('Serving From Cache: ' + event.request.url);
        return cachedResponse;
    }

    if (!navigator.onLine) {
        // log('User is offline, serving fallback page.');
        return staticCache.match('fallback.html');
    }

    const networkResponse = await fetch(event.request);

    // log('Calling network: ' + event.request.url);

    const isManifestLink = networkResponse.url === 'http://' + location.host + '/notification.json'

    if (networkResponse && networkResponse.status === 200 && !isManifestLink) {
        dynamicCache.put(event.request, networkResponse.clone());
    }

    return networkResponse;
}



// ----------------- notificationclick -----------------
self.addEventListener('notificationclick', function (event) {
    event.notification.close();

    if (event.notification.data.url) {
        event.waitUntil(
            clients.openWindow(event.notification.data.url)
        );
    }
});



// ----------------- log -----------------



// function log(message) {
//     console.log(VERSION, message);
// }