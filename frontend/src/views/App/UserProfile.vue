<template>
  <div class="profile-page">
    <TheHeader />

    <div class="profile-container">
      <h1>Manage Your Profile</h1>
      <p class="description">Update your account details below.</p>

      <!-- Options for Update Email and Password -->
      <div class="update-options">
        <button @click="showUpdateSection('email')" class="update-button">Update Email</button>
        <button @click="showUpdateSection('password')" class="update-button">Update Password</button>
      </div>

      <form @submit.prevent="updateProfile" class="profile-form">
        <!-- Email Section (with two fields for current and new email) -->
        <div v-if="activeSection === 'email'" class="email-section">
          <label for="current-email" class="profile-label">Current Email</label>
          <input
            id="current-email"
            type="email"
            class="email-input"
            v-model="profile.currentEmail"
            placeholder="Enter your current email"
            required
          />
          <label for="new-email" class="profile-label">New Email</label>
          <input
            id="new-email"
            type="email"
            class="email-input"
            v-model="profile.newEmail"
            placeholder="Enter your new email"
            required
          />
        </div>

        <!-- Password Section (with two fields for current and new password) -->
        <div v-if="activeSection === 'password'" class="password-section">
          <label for="current-password" class="profile-label">Current Password</label>
          <input
            id="current-password"
            type="password"
            class="password-input"
            v-model="profile.currentPassword"
            placeholder="Enter your current password"
            required
          />
          <label for="new-password" class="profile-label">New Password</label>
          <input
            id="new-password"
            type="password"
            class="password-input"
            v-model="profile.newPassword"
            placeholder="Enter your new password"
            required
          />
        </div>


        <!-- Profile Picture Section -->

        <!-- Submit Button -->
        <div class="form-actions">
          <button type="submit" class="save-button" :disabled="isSaving">
            <span v-if="!isSaving">Save Changes</span>
            <span v-else>Saving...</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import TheHeader from "@/components/AppComponents/TheHeader.vue";
import axios from "axios";
import Swal from "sweetalert2";

export default {
  name: "UserProfile",
  components: {
    TheHeader,
  },
  data() {
    return {
      profile: {
        currentEmail: "",
        newEmail: "",
        profilePicture: null,
      },
      previewImage: null,
      profilePictureFile: null,
      isSaving: false,
      activeSection: null, // Tracks the currently active section
    };
  },
  methods: {
    showUpdateSection(section) {
      this.activeSection = section;
    },
    updateProfile() {
      if (this.profile.currentEmail === this.profile.newEmail) {
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "The current email and new email cannot be the same.",
        });
        return;
      }

      this.isSaving = true;
      const formData = new FormData();
      formData.append("currentEmail", this.profile.currentEmail);
      formData.append("newEmail", this.profile.newEmail);

      axios
        .post("http://127.0.0.1:5000/api/update-profile", formData, {
          withCredentials: true,
          headers: {
            "X-CSRF-TOKEN": localStorage.getItem("csrfToken"),
          },
        })
        .then((response) => {
          if (response.data.success) {
            Swal.fire({
              position: "top-end",
              toast: true,
              icon: "success",
              title: "Email has been updated",
              showConfirmButton: false,
              timer: 3000,
            });
          } else {
            Swal.fire({
              icon: "error",
              title: "Error",
              text: response.data.message || "Failed to update profile.",
            });
          }
        })
        .catch((error) => {
          console.error("Error updating profile:", error);
          Swal.fire({
            icon: "error",
            title: "Error",
            text: "Error updating profile. Please try again.",
          });
        })
        .finally(() => {
          this.isSaving = false;
        });
    },
  },
};
</script>


<style scoped>
.profile-page {
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  min-height: 100vh;
  padding: 0;
}

.profile-container {
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 2rem;
  color: #2c64ff;
  margin-bottom: 10px;
  text-align: center;
}

.description {
  font-size: 1rem;
  color: #666;
  text-align: center;
  margin-bottom: 30px;
}

.profile-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.profile-label {
  font-size: 1rem;
  color: #2c64ff;
  font-weight: bold;
  margin-bottom: 5px;
}

.email-section {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.email-input {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.password-section {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.password-input {
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.form-actions {
  text-align: center;
}

.save-button {
  background-color: #2c64ff;
  color: #fff;
  font-size: 1rem;
  font-weight: bold;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s ease-in-out;
}

.update-options {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  justify-content: center;
}

.update-button {
  background-color: #2c64ff;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
}

.save-button:hover {
  background-color: #1a47d5;
}
</style>
