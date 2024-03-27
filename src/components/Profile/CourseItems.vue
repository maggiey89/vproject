<template>
    <li>
        <div class="course">
            <!--input v-if="course.isEditing" type="text" :value="course.course" 
                @input="$emit('update-course', $event.target.value, index)"/>
            <span v-else>
                {{ course.course }}
            </span-->
            <span>
                {{ course.course }}
            </span>
        </div>
        <div class="course-actions">
            <!--Icon v-if="course.isEditing" icon="ph:check-circle" 
                color="#41b080" width="15px" @click="$emit('edit-course', index)"/>
            <Icon v-else icon="ph:pencil-fill" 
                color="#41b080" width="15px" @click="$emit('edit-course', index)"/-->
            <Icon icon="ph:trash" 
                color="#f95e5e" width="15px" @click="$emit('delete-course', course.id)"/>
        </div>
    </li>

</template>

<script setup>
import { Icon } from '@iconify/vue'

const props = defineProps({
    course: {
        type: Object,
        required: true,
    },
    index: {
        type: Number,
        required: true,
    },
});

defineEmits(["edit-course", "update-course", "delete-course"]);
</script>

<style>
li {
    display: flex;
    text-align: left;
    align-items: center;
    gap: 6px;
    width: fit-content;
    height: fit-content;
    &:hover {
        .course-actions {
            opacity: 1;
        }
    }

    .course {
        flex: 1;
        input[type="text"] {
            width: 100%;
            height: 100%;
            border: 2px solid;
            text-underline-position: below;
        }
    }

    .course-actions {
        display: flex;
        gap: 6px;
        opacity: 0;
        transition: 150ms ease-in-out;
        cursor: pointer;
    }
}
</style>