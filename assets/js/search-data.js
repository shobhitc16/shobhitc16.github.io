// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-research",
          title: "research",
          description: "Understanding enzyme catalysis, predicting and engineering enzyme function, and applying frontier methods toward sustainable chemistry and human health.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "Publications in reversed chronological order, generated from BibTeX via jekyll-scholar.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-teaching",
          title: "teaching",
          description: "Teaching experience, mentoring activities, and professional service.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching/";
          },
        },{id: "nav-awards",
          title: "awards",
          description: "Awards, fellowships, computational grants, and professional activities.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/awards/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "Academic curriculum vitae of Shobhit S. Chaturvedi.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "news-joined-the-alexandrova-group-at-ucla-as-a-postdoctoral-scholar-in-the-department-of-chemistry-amp-amp-biochemistry-excited-to-investigate-enzyme-catalysis-through-electric-fields-and-machine-learning",
          title: 'Joined the Alexandrova Group at UCLA as a Postdoctoral Scholar in the Department...',
          description: "",
          section: "News",},{id: "news-our-review-on-the-role-of-second-coordination-sphere-residues-in-metalloenzyme-catalysis-is-published-in-chemical-science-2023-14-8027-8046",
          title: 'Our review on the role of second coordination sphere residues in metalloenzyme catalysis...',
          description: "",
          section: "News",},{id: "news-our-paper-on-electric-field-evolution-through-directed-evolution-of-protoglobin-for-carbene-transfer-has-been-published-in-j-am-chem-soc-2024-146-16670-16680",
          title: 'Our paper on electric field evolution through directed evolution of protoglobin for carbene...',
          description: "",
          section: "News",},{id: "news-new-paper-in-jacs-our-machine-learning-framework-interprets-3d-electric-fields-across-heme-iron-oxidoreductases-to-predict-enzymatic-function-published-in-j-am-chem-soc-2024-146-28375-28383",
          title: 'New paper in JACS: Our machine learning framework interprets 3D electric fields across...',
          description: "",
          section: "News",},{id: "news-our-comprehensive-review-on-electric-fields-in-enzyme-catalysis-has-been-published-in-chemical-reviews-2025-this-review-covers-the-theory-computational-methods-and-experimental-measurements-of-electric-fields-in-enzymatic-systems",
          title: 'Our comprehensive review on electric fields in enzyme catalysis has been published in...',
          description: "",
          section: "News",},{id: "news-pycpet-our-open-source-python-toolbox-for-computing-heterogeneous-3d-protein-electric-fields-has-been-published-in-the-journal-of-chemical-theory-and-computation-jctc-2025",
          title: 'PyCPET — our open-source Python toolbox for computing heterogeneous 3D protein electric fields...',
          description: "",
          section: "News",},{id: "news-joined-eth-zurich-as-a-postdoctoral-scholar-in-the-department-of-chemistry-and-applied-biosciences-working-on-quantum-computing-for-biology-automated-reaction-network-exploration-and-metalloenzyme-engineering",
          title: 'Joined ETH Zurich as a Postdoctoral Scholar in the Department of Chemistry and...',
          description: "",
          section: "News",},{
        id: 'social-cv',
        title: 'CV',
        section: 'Socials',
        handler: () => {
          window.open("/assets/pdf/Chaturvedi_CV.pdf", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%73%68%6F%62%68%69%74%73%63%68%61%74%75%72%76%65%64%69@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/shobhitc16", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/shobhit-s-chaturvedi", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0003-4977-5600", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=9XyXnhIAAAAJ", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
