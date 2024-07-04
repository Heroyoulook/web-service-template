<template>
  <div id="app">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <!-- Toggle button for sidebar -->
        <button class="navbar-toggler" type="button" @click="toggleSidebar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <a class="navbar-brand" href="#">Navbar</a>
        <!-- Button or link on the left side -->
        <button class="btn btn-outline-light d-lg-none" @click="toggleSidebar">
          <i class="fas fa-bars"></i>
        </button>
      </div>
    </nav>

    <!-- Sidebar -->
    <nav class="navbar navbar-dark bg-dark sidebar" :class="{ 'show': isSidebarOpen }" ref="sidebar">
      <div class="container-fluid">
        <!-- Sidebar content -->
        <ul class="navbar-nav flex-column">
          <!-- Example links -->
          <li class="nav-item">
            <a class="nav-link" href="#">Link 1</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link 2</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link 3</a>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Main content area -->
    <div class="main-content" :class="{ 'pushed': isSidebarOpen }">
      <!-- Your main content goes here -->
      <div class="container" @click="closeSidebar">
        <h1>Main Content</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isSidebarOpen: false
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },
    closeSidebar(event) {
      // Check if the click occurred outside the sidebar
      if (this.isSidebarOpen && !this.$refs.sidebar.contains(event.target)) {
        this.isSidebarOpen = false;
      }
    }
  }
}
</script>

<style scoped>
/* Custom styles for the sidebar */
.sidebar {
  width: 250px;
  /* Adjust sidebar width */
  position: fixed;
  top: 0;
  left: -250px;
  /* Start off-screen */
  bottom: 0;
  background-color: #343a40;
  /* Dark background color */
  transition: left 0.3s ease-in-out;
}

.sidebar .container-fluid {
  padding: 15px;
  /* Optional padding */
}

.sidebar .navbar-nav {
  margin-top: 20px;
  /* Optional margin */
}

.sidebar .nav-link {
  color: #fff;
}

.sidebar.show {
  left: 0;
  /* Slide sidebar in */
}

/* Custom styles for the main content */
.main-content {
  transition: margin-left 0.3s ease-in-out;
  margin-left: 0;
  padding: 20px;
}

.main-content.pushed {
  margin-left: 250px;
  /* Adjust based on sidebar width */
}

/* Custom styles for the sidebar toggle button on small screens */
@media (min-width: 992px) {
  .btn-outline-light.d-lg-none {
    display: none;
    /* Hide the toggle button on larger screens */
  }
}
</style>
