// @ts-check

const config = {
  title: 'Maoruanx Wiki',
  tagline: '游戏作弊器教程百科',
  favicon: 'img/favicon.ico',
  url: 'https://maldita-wiki.github.io',
  baseUrl: '/maoruanx-wiki/',
  organizationName: 'Maldita-wiki',
  projectName: 'maoruanx-wiki',
  onBrokenLinks: 'warn',
  i18n: {
    defaultLocale: 'zh-Hans',
    locales: ['zh-Hans'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: false,
      },
    ],
  ],
};

module.exports = config;