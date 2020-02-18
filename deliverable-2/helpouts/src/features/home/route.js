import {
  HomePage
} from './';

export default {
  path: '/',
  name: 'Home',
  childRoutes: [
    { path: '',
      name: 'Home page',
      component: HomePage,
      isIndex: true,
    },
  ],
};
