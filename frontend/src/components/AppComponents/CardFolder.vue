<template>
  <div class="folder-wrapper">
    <div class="folder" :class="[size, backgroundColor]">
      <div class="folder__top"></div>
      <div class="folder__bottom">
        <div v-if="havePlus" class="plus-icon plus-icon--black"></div>
        <div
          class="description"
          v-if="showDescription"
          data-folder-action="open-folder"
        >
          <div class="title" v-if="projectName">
            {{ projectName }}
          </div>
          <span
            class="trash-icon trash-icon--black"
            v-if="trash"
            data-folder-action="delete"
          ></span>
          <div class="owner" v-if="owner">
            {{ owner }}
          </div>
          <div class="visibility" v-if="visibility == 'private'">
            <span
              class="visibility__icon visibility__icon--private"
              title="Private"
            ></span>
            <!--            <span class="visibility__text">Private</span>-->
          </div>
          <div class="visibility" v-if="visibility == 'public'">
            <span
              class="visibility__icon visibility__icon--public"
              title="Public"
            ></span>
            <!--            <span class="visibility__text">Public</span>-->
          </div>
        </div>
      </div>
    </div>
    <span class="bottom-text" v-if="bottomText && bottomText.show">{{
      bottomText.text
    }}</span>
  </div>
</template>

<script>
// TODO: Expand CardFolder to be two components - CardFolderSmall and CardFolderBig; Also, add folder color to DB when migrating

export default {
  name: "CardFolder",
  props: {
    size: String,
    backgroundColor: String,
    havePlus: Boolean,
    showDescription: Boolean,
    projectName: String,
    owner: String,
    visibility: String,
    trash: Boolean,
    bottomText: {
      show: Boolean,
      text: String,
    },
  },
};
</script>

<style lang="scss" scoped>
.folder-wrapper {
  width: min-content;
}

.bottom-text {
  display: inline-block;
  margin-top: 10px;
  font-weight: 300;
  color: #808080;
}

.folder {
  $block: &;
  background-color: transparent;

  &__top {
    background-color: transparent;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    border-bottom-style: solid;
    border-right-style: solid;
    border-right-color: transparent;
    cursor: pointer;
    transition: 0.3s ease-in-out;
  }

  &__bottom {
    width: 100%;
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
    border-top-right-radius: 8px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: 0.3s ease-in-out;
  }

  &--green {
    #{$block}__top {
      border-bottom-color: $folder-green;
    }

    #{$block}__bottom {
      border: 2px solid $folder-green;

      &:hover {
        background-color: $folder-green;
      }
    }
  }

  &--lightblue {
    #{$block}__top {
      border-bottom-color: $folder-lightblue;
    }

    #{$block}__bottom {
      border: 2px solid $folder-lightblue;

      &:hover {
        background-color: $folder-lightblue;
      }
    }
  }

  &--darkblue {
    #{$block}__top {
      border-bottom-color: $folder-darkblue;
    }

    #{$block}__bottom {
      border: 2px solid $folder-darkblue;

      &:hover {
        background-color: $folder-darkblue;
      }
    }
  }

  &--lightorange {
    #{$block}__top {
      border-bottom-color: $folder-lightorange;
    }

    #{$block}__bottom {
      border: 2px solid $folder-lightorange;

      &:hover {
        background-color: $folder-lightorange;
      }
    }
  }

  &--darkorange {
    #{$block}__top {
      border-bottom-color: $folder-darkorange;
    }

    #{$block}__bottom {
      border: 2px solid $folder-darkorange;

      &:hover {
        background-color: $folder-darkorange;
      }
    }
  }

  &--yellow {
    #{$block}__top {
      border-bottom-color: $folder-yellow;
    }

    #{$block}__bottom {
      border: 2px solid $folder-yellow;

      &:hover {
        background-color: $folder-yellow;
      }
    }
  }

  &--gray {
    #{$block}__top {
      border-bottom-color: #bfd0ff;
    }

    #{$block}__bottom {
      border: 2px solid #bfd0ff;

      &:hover {
        background-color: #bfd0ff;
      }
    }
  }

  &--small {
    width: 163px;
    height: 100px;

    #{ $block }__top {
      width: 50px;
      height: 8px; // top + bottom height should add up to .folder height
      border-bottom-width: 8px;
      border-right-width: 8px;
    }

    #{ $block }__bottom {
      height: 92px; // top + bottom height should add up to .folder height
    }
  }

  &--large {
    width: 300px;
    height: 200px;

    #{ $block }__top {
      width: 100px;
      height: 16px; // top + bottom height should add up to .folder height
      border-bottom-width: 16px;
      border-right-width: 16px;
    }

    #{ $block }__bottom {
      height: 184px; // top + bottom height should add up to .folder height
    }
  }
}

.description {
  width: 100%;
  height: 100%;
  padding: 20px;
  display: flex;
  align-content: space-between;
  justify-content: space-between;
  flex-wrap: wrap;
  color: #596389;
  // font-family: "Inconsolata";

  .title {
    display: inline-block;
    font-weight: 700;
    font-size: 20px;
    flex: 90%;
  }

  //.more-icon {
  //  background: url("../../assets/images/more-horizontal.svg");
  //  background-size: 25px;
  //  background-position: center;
  //  background-repeat: no-repeat;
  //  height: 25px;
  //  width: 25px;
  //  flex-shrink: 0;
  //}

  .owner {
    font-weight: 300;
    line-height: 20px;
    // font-style: ;
  }

  .visibility {
    display: flex;
    align-content: center;
    column-gap: 3px;

    &__icon {
      display: inline-block;
      background-size: 20px;
      background-position: center;
      background-repeat: no-repeat;
      height: 20px;
      width: 20px;

      &--public {
        background-image: url("../../assets/images/globe.svg");
      }

      &--private {
        background-image: url("../../assets/images/lock.svg");
      }
    }

    &__text {
      display: inline-block;
      padding-top: 2px;
    }
  }
}

.folder--small {
  .description {
    .title {
      font-size: 16px;
    }
  }
}
</style>
