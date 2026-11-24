<template>
  <NuxtLayout name="dashboard">
    <div class="space-y-6 max-w-3xl">
      <div>
        <h1 class="text-2xl font-black text-gray-900 dark:text-white">نقل ملفات Bunny</h1>
        <p class="text-sm text-gray-500 mt-2 leading-relaxed">
          ينسخ ملفات الموقع من مساحة التخزين القديمة إلى مساحة الشركة
          <span dir="ltr" class="font-mono">{{ info?.zone }}</span>.
          القراءة من العنوان القديم عامة، والكتابة بالمفتاح الجديد وحده.
          التشغيل آمن ويمكن تكراره: الملف الموجود مسبقاً يُتخطّى.
        </p>
      </div>

      <div v-if="info" class="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl border border-gray-100 dark:border-gray-700">
          <div class="text-xs font-bold text-gray-400 mb-1">إجمالي الملفات</div>
          <div class="text-2xl font-black text-gray-900 dark:text-white">{{ info.total }}</div>
        </div>
        <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl border border-gray-100 dark:border-gray-700">
          <div class="text-xs font-bold text-gray-400 mb-1">نُسخت</div>
          <div class="text-2xl font-black text-green-600">{{ copied }}</div>
        </div>
        <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl border border-gray-100 dark:border-gray-700">
          <div class="text-xs font-bold text-gray-400 mb-1">موجودة مسبقاً</div>
          <div class="text-2xl font-black text-gray-500">{{ exists }}</div>
        </div>
        <div class="bg-white dark:bg-gray-800 p-4 rounded-2xl border border-gray-100 dark:border-gray-700">
          <div class="text-xs font-bold text-gray-400 mb-1">فشلت</div>
          <div class="text-2xl font-black" :class="failed.length ? 'text-red-600' : 'text-gray-500'">{{ failed.length }}</div>
        </div>
      </div>

      <div v-if="info && !info.keyConfigured" class="p-4 rounded-2xl bg-red-50 text-red-800 text-sm font-bold">
        المتغير BUNNY_NEW_STORAGE_KEY غير مضبوط في هذه البيئة، فلا يمكن الكتابة.
      </div>

      <div class="flex flex-wrap items-center gap-3">
        <button
          type="button"
          class="px-6 h-12 rounded-xl bg-primary text-white font-bold disabled:opacity-50"
          :disabled="running || !info?.keyConfigured"
          @click="run"
        >
          {{ running ? 'جارٍ النقل…' : (done ? 'إعادة التشغيل' : 'ابدأ النقل') }}
        </button>
        <button
          v-if="running"
          type="button"
          class="px-6 h-12 rounded-xl border border-gray-300 font-bold"
          @click="stop = true"
        >
          إيقاف
        </button>
        <span class="text-sm text-gray-500">{{ processed }} من {{ info?.total || 0 }}</span>
      </div>

      <div v-if="info?.total" class="h-2 rounded-full bg-gray-200 overflow-hidden">
        <div class="h-full bg-primary transition-all" :style="{ width: pct + '%' }"></div>
      </div>

      <div v-if="failed.length" class="space-y-2">
        <h2 class="font-bold text-red-700">ملفات فشلت</h2>
        <ul class="text-xs font-mono bg-red-50 rounded-xl p-4 space-y-1 max-h-72 overflow-auto" dir="ltr">
          <li v-for="f in failed" :key="f.path">{{ f.path }} — {{ f.detail }}</li>
        </ul>
      </div>

      <div v-if="done" class="p-4 rounded-2xl bg-green-50 text-green-800 text-sm font-bold">
        انتهى النقل. تحقّق من فتح الملفات على
        <span dir="ltr" class="font-mono">{{ info?.cdn }}</span>
        قبل استبدال الروابط في الموقع.
      </div>
    </div>
  </NuxtLayout>
</template>

<script setup lang="ts">
definePageMeta({ layout: false, middleware: 'auth' })
useHead({ title: 'نقل ملفات Bunny' })

type Info = { zone: string, cdn: string, keyConfigured: boolean, total: number }
type Failure = { path: string, detail?: string }

const info = ref<Info | null>(null)
const running = ref(false)
const stop = ref(false)
const done = ref(false)
const processed = ref(0)
const copied = ref(0)
const exists = ref(0)
const failed = ref<Failure[]>([])

const pct = computed(() => info.value?.total ? Math.round((processed.value / info.value.total) * 100) : 0)

onMounted(async () => {
  info.value = await $fetch<Info>('/api/admin/migrate-cdn')
})

async function run() {
  running.value = true
  stop.value = false
  done.value = false
  processed.value = 0
  copied.value = 0
  exists.value = 0
  failed.value = []

  let offset = 0
  try {
    while (!stop.value) {
      const res = await $fetch<any>('/api/admin/migrate-cdn', {
        method: 'POST',
        body: { offset, limit: 10 }
      })
      offset = res.nextOffset
      processed.value = offset
      copied.value += res.copied
      exists.value += res.exists
      if (res.failed?.length) failed.value.push(...res.failed)
      if (res.done) { done.value = true; break }
    }
  } finally {
    running.value = false
  }
}
</script>
