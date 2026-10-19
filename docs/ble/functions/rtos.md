# BLE - `rtos` functions

102 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`app_noop_hook_0c0427f0`](#app_noop_hook_0c0427f0) | 0x0C0427F0 | Empty function (single return), never called directly |
| [`ble_bt_stack_task_create`](#ble_bt_stack_task_create) | 0x0C05B6CC | Create the 'bt stack' RTOS task with entry 0x0C05B678 and a 1 KiB stack |
| [`ble_evt_clear_index_bit`](#ble_evt_clear_index_bit) | 0x0C048298 | Clear the event bit that ble_evt_set_index_bit sets, via xEventGroupClearBits |
| [`ble_evt_read_bits`](#ble_evt_read_bits) | 0x0C0482B8 | Return the whole BLE event group value when the index bit is valid, else 0 |
| [`ble_evt_set_index_bit`](#ble_evt_set_index_bit) | 0x0C048278 | Set event bit 2*index + (selector & 1) in the BLE event group at 0x2000F6D4 |
| [`ble_sched_check_and_pend_pendsv`](#ble_sched_check_and_pend_pendsv) | 0x0C05D0C4 | Request a PendSV exception when the scheduler object reports pending work |
| [`ble_sched_signal_event`](#ble_sched_signal_event) | 0x0C05D494 | Signal event 1 on the BLE scheduler object at 0x20017184 |
| [`ble_signal_worker_event`](#ble_signal_worker_event) | 0x0C059938 | Signal the BLE worker event handle held in the global at 0x20014564 |
| [`ble_stack_lock_give`](#ble_stack_lock_give) | 0x0C046EC0 | Release the shared BLE stack mutex taken by ble_stack_lock_take |
| [`ble_stack_lock_take`](#ble_stack_lock_take) | 0x0C046E88 | Take the shared BLE stack mutex, creating it on first use while the scheduler runs |
| [`pcTaskGetName`](#pctaskgetname) | 0x0C043F34 | FreeRTOS: return pointer to a task's name string |
| [`posix_event_2000f65c_init`](#posix_event_2000f65c_init) | 0x0C047F70 | Static constructor: initialise the RTOS event object at 0x2000F660 and store its handle in 0x2000F65C |
| [`posix_select_event_init`](#posix_select_event_init) | 0x0C048260 | Static constructor: initialise the RTOS event object that the fd-layer select() waits on |
| [`prvAddCurrentTaskToDelayedList`](#prvaddcurrenttasktodelayedlist) | 0x0C043A7C | FreeRTOS: move the running task to the delayed, overflow-delayed or suspended list |
| [`prvAddNewTaskToReadyList`](#prvaddnewtasktoreadylist) | 0x0C043978 | FreeRTOS: register a freshly created TCB with the scheduler and put it on its ready list |
| [`prvCheckForValidListAndQueue`](#prvcheckforvalidlistandqueue) | 0x0C044AA4 | Create the timer lists and the timer command queue (8 x 16 bytes) once, under a critical section |
| [`prvCopyDataToQueue`](#prvcopydatatoqueue) | 0x0C042A3C | FreeRTOS queue.c: copy an item into the queue at back/front/overwrite position, or release a mutex |
| [`prvInitialiseMutex`](#prvinitialisemutex) | 0x0C042D80 | Initialise a static one-slot, zero-item-size queue as a mutex or semaphore and give its token |
| [`prvInitialiseNewQueue`](#prvinitialisenewqueue) | 0x0C042BA0 | FreeRTOS queue.c: fill a static Queue_t (length, item size, storage, type) and reset it |
| [`prvInitialiseNewTask`](#prvinitialisenewtask) | 0x0C043BA8 | FreeRTOS: fill a TCB, paint the stack and build the initial context for a new task |
| [`prvInsertTimerInActiveList`](#prvinserttimerinactivelist) | 0x0C044BB0 | FreeRTOS timers: queue a software timer in the current or overflow timer list |
| [`prvIsQueueEmpty`](#prvisqueueempty) | 0x0C043364 | FreeRTOS queue: true when no messages are waiting |
| [`prvIsQueueFull`](#prvisqueuefull) | 0x0C043370 | FreeRTOS queue: true when uxMessagesWaiting equals uxLength |
| [`prvListTasksWithinSingleList`](#prvlisttaskswithinsinglelist) | 0x0C0444F4 | FreeRTOS prvListTasksWithinSingleList: append a TaskStatus_t for each task of one list |
| [`prvReadBytesFromBuffer`](#prvreadbytesfrombuffer) | 0x0C043414 | FreeRTOS stream_buffer.c: copy min(xMaxCount, xBytesAvailable) bytes out of the circular buffer at xTail |
| [`prvSwitchTimerLists`](#prvswitchtimerlists) | 0x0C044DE8 | Run the timers in the current list and swap the current and overflow timer lists |
| [`prvUnlockQueue`](#prvunlockqueue) | 0x0C042AAC | FreeRTOS queue.c: unlock a queue, waking tasks blocked on receive/send for each pending lock count |
| [`prvWriteBytesToBuffer`](#prvwritebytestobuffer) | 0x0C0433D0 | FreeRTOS stream_buffer.c: copy xCount bytes into the circular buffer at xHead with wrap-around |
| [`pvTaskIncrementMutexHeldCount`](#pvtaskincrementmutexheldcount) | 0x0C0447D0 | FreeRTOS: increment the running task's mutex-held counter |
| [`rtos_enter_critical`](#rtos_enter_critical) | 0x0C03F874 | Raise BASEPRI to 0x40 and return the previous value (start of critical section) |
| [`rtos_exit_critical`](#rtos_exit_critical) | 0x0C03F88C | Restore BASEPRI to a saved value (end of critical section) |
| [`rtos_mutex_give_checked`](#rtos_mutex_give_checked) | 0x0C042E20 | Release a non-recursive mutex the caller holds: clear the recursion count and send the token |
| [`rtos_pendsv_trigger`](#rtos_pendsv_trigger) | 0x0C03F628 | Pend the PendSV exception to request a context switch |
| [`rtos_pool_node_alloc_init`](#rtos_pool_node_alloc_init) | 0x0C04211C | Pop a node from a free list under a BASEPRI critical section and initialise it |
| [`rtos_port_yield_from_isr`](#rtos_port_yield_from_isr) | 0x0C04583C | Cortex-M: pend PendSV when param_1 is non-zero (portYIELD_FROM_ISR) |
| [`rtos_run_time_counter_get`](#rtos_run_time_counter_get) | 0x0C046290 | Thunk to RAM patch 0x20000328: read the run-time-stats counter for FreeRTOS |
| [`rtos_start_first_task`](#rtos_start_first_task) | 0x0C03F850 | Reset MSP from the vector table, enable interrupts and trigger SVC #2 to start the scheduler |
| [`rtos_systick_sub_tick_ns`](#rtos_systick_sub_tick_ns) | 0x0C03F790 | Nanoseconds elapsed inside the current 1 ms SysTick period, +1 ms if the COUNTFLAG shows a wrap |
| [`rtos_task_stack_init`](#rtos_task_stack_init) | 0x0C03F6C4 | Build the initial context frame on a new task stack and return the new stack pointer |
| [`rtos_timer_pend_fixed_callback_from_isr`](#rtos_timer_pend_fixed_callback_from_isr) | 0x0C042988 | ISR-safe post of a fixed deferred callback with two arguments to the timer daemon queue |
| [`stream_buffer_commit_head`](#stream_buffer_commit_head) | 0x0C0438D8 | Advance a stream buffer's head by up to N free bytes and wake a receiver at the trigger level |
| [`stream_buffer_consume_tail`](#stream_buffer_consume_tail) | 0x0C043830 | Advance a stream buffer's tail by up to N stored bytes and wake a sender waiting for space |
| [`uxListRemove`](#uxlistremove) | 0x0C042A14 | FreeRTOS: unlink an item from the list that contains it |
| [`uxQueueMessagesWaiting`](#uxqueuemessageswaiting) | 0x0C043320 | FreeRTOS: number of items currently in the queue, read inside a critical section |
| [`uxQueueSpacesAvailable`](#uxqueuespacesavailable) | 0x0C043338 | FreeRTOS: free slots in a queue (uxLength - uxMessagesWaiting) read inside a critical section |
| [`uxTaskGetNumberOfTasks`](#uxtaskgetnumberoftasks) | 0x0C043F28 | Return the RTOS word at DAT_2000cc14 (likely the number of tasks) |
| [`uxTaskGetSystemState`](#uxtaskgetsystemstate) | 0x0C044544 | FreeRTOS uxTaskGetSystemState: snapshot TaskStatus_t entries for every task and the total run time |
| [`uxTaskResetEventItemValue`](#uxtaskreseteventitemvalue) | 0x0C0447B8 | FreeRTOS: return and reset the current task's event list item value |
| [`vApplicationGetIdleTaskMemory`](#vapplicationgetidletaskmemory) | 0x0C042800 | Provide static TCB and stack buffers for the idle task (FreeRTOS static allocation) |
| [`vListInitialise`](#vlistinitialise) | 0x0C0429A4 | FreeRTOS: initialise an empty list with its end marker |
| [`vListInitialiseItem`](#vlistinitialiseitem) | 0x0C0429BC | FreeRTOS: mark a list item as not belonging to any list |
| [`vListInsert`](#vlistinsert) | 0x0C0429E4 | FreeRTOS: insert an item into a list sorted by xItemValue |
| [`vListInsertEnd`](#vlistinsertend) | 0x0C0429C4 | FreeRTOS: insert an item at the end of a list (before pxIndex) |
| [`vPortEnterCritical`](#vportentercritical) | 0x0C03F640 | FreeRTOS port: raise BASEPRI, increment uxCriticalNesting (DAT_20003ec4), DSB+ISB |
| [`vPortExitCritical`](#vportexitcritical) | 0x0C03F65C | FreeRTOS port: decrement uxCriticalNesting (DAT_20003ec4) and re-enable interrupts when it reaches 0 |
| [`vPortSetupTimerInterrupt`](#vportsetuptimerinterrupt) | 0x0C03F600 | FreeRTOS port: program SysTick for a 1 ms tick (LOAD = clk/1000 - 1, CTRL = ENABLE\|TICKINT) |
| [`vQueueWaitForMessageRestricted`](#vqueuewaitformessagerestricted) | 0x0C043380 | FreeRTOS vQueueWaitForMessageRestricted: block the caller on an empty queue without a wake-up time |
| [`vTaskDelay`](#vtaskdelay) | 0x0C0441A8 | FreeRTOS vTaskDelay: block the calling task for a number of ticks, with zero only yielding |
| [`vTaskGetInfo`](#vtaskgetinfo) | 0x0C044400 | FreeRTOS vTaskGetInfo: fill a TaskStatus_t for a task, deriving its state and stack high-water mark |
| [`vTaskInternalSetTimeOutState`](#vtaskinternalsettimeoutstate) | 0x0C044360 | FreeRTOS: record overflow count and tick count in a TimeOut_t |
| [`vTaskMissedYield`](#vtaskmissedyield) | 0x0C0443F4 | FreeRTOS: flag that a context switch was requested while the scheduler was suspended |
| [`vTaskPlaceOnEventList`](#vtaskplaceoneventlist) | 0x0C0441F0 | FreeRTOS: block the current task on a sorted event list with a timeout |
| [`vTaskPlaceOnEventListRestricted`](#vtaskplaceoneventlistrestricted) | 0x0C044238 | FreeRTOS: block the current task on an event list, optionally forever (timer task) |
| [`vTaskPlaceOnUnorderedEventList`](#vtaskplaceonunorderedeventlist) | 0x0C044210 | FreeRTOS: block the current task on an unordered event list (event groups) |
| [`vTaskPriorityDisinheritAfterTimeout`](#vtaskprioritydisinheritaftertimeout) | 0x0C044744 | FreeRTOS: lower a mutex holder's priority after a waiter timed out |
| [`vTaskRemoveFromUnorderedEventList`](#vtaskremovefromunorderedeventlist) | 0x0C0442E4 | FreeRTOS: wake a task from an unordered event list and hand it the result value |
| [`vTaskSetTimeOutState`](#vtasksettimeoutstate) | 0x0C04433C | FreeRTOS: record overflow count and tick count in a TimeOut_t inside a critical section |
| [`vTaskSuspendAll`](#vtasksuspendall) | 0x0C043F0C | FreeRTOS: suspend the scheduler by incrementing the nesting counter |
| [`xEventGroupClearBits`](#xeventgroupclearbits) | 0x0C042900 | FreeRTOS: clear bits in an event group inside a critical section and return the previous value |
| [`xEventGroupCreateStatic`](#xeventgroupcreatestatic) | 0x0C04281C | FreeRTOS: initialise a caller-provided StaticEventGroup_t and return it as the event group handle |
| [`xEventGroupSetBits`](#xeventgroupsetbits) | 0x0C04291C | FreeRTOS xEventGroupSetBits: OR bits into the group and wake matching waiters |
| [`xEventGroupWaitBits`](#xeventgroupwaitbits) | 0x0C042858 | FreeRTOS xEventGroupWaitBits: wait for event bits, blocking on the group's unordered list |
| [`xQueueGenericReset`](#xqueuegenericreset) | 0x0C042B38 | FreeRTOS queue.c: reset a queue to empty and (optionally) re-initialise its wait lists |
| [`xQueueGenericSend`](#xqueuegenericsend) | 0x0C042C8C | FreeRTOS xQueueGenericSend: copy an item into a queue, blocking up to a tick timeout when full |
| [`xQueueGenericSendFromISR`](#xqueuegenericsendfromisr) | 0x0C042EB4 | FreeRTOS xQueueGenericSendFromISR: queue an item from interrupt context inside a critical section |
| [`xQueueGiveFromISR`](#xqueuegivefromisr) | 0x0C042F38 | FreeRTOS queue.c: give a semaphore from an ISR, waking a waiting receiver if the queue is unlocked |
| [`xQueueGiveMutexRecursive`](#xqueuegivemutexrecursive) | 0x0C042DF4 | FreeRTOS xQueueGiveMutexRecursive: release one level of a recursive mutex the caller holds |
| [`xQueuePeek`](#xqueuepeek) | 0x0C043224 | FreeRTOS xQueuePeek: copy the head item to a buffer without removing it, with optional blocking |
| [`xQueueReceive`](#xqueuereceive) | 0x0C042FA4 | FreeRTOS xQueueReceive: dequeue one item into a buffer, blocking up to a tick timeout when empty |
| [`xQueueSemaphoreTake`](#xqueuesemaphoretake) | 0x0C0430A8 | FreeRTOS xQueueSemaphoreTake: take a semaphore or mutex token, with priority inheritance for mutexes |
| [`xQueueTakeMutexRecursive`](#xqueuetakemutexrecursive) | 0x0C0431F8 | FreeRTOS xQueueTakeMutexRecursive: take a recursive mutex, re-entering when the caller already holds it |
| [`xStreamBufferGenericCreateStatic`](#xstreambuffergenericcreatestatic) | 0x0C043498 | FreeRTOS: initialise a static stream/message buffer (size, trigger level, storage, flags) |
| [`xStreamBufferReceive`](#xstreambufferreceive) | 0x0C0436F8 | FreeRTOS xStreamBufferReceive: read a stream or message from a buffer, blocking until data arrives |
| [`xStreamBufferReset`](#xstreambufferreset) | 0x0C0434E8 | FreeRTOS: empty a stream buffer if no task is blocked on it, keeping buffer, length, trigger level and number |
| [`xStreamBufferSend`](#xstreambuffersend) | 0x0C043554 | FreeRTOS xStreamBufferSend: write a stream or message into a buffer, blocking for free space |
| [`xStreamBufferSendFromISR`](#xstreambuffersendfromisr) | 0x0C043658 | FreeRTOS: copy data into a stream/message buffer from an ISR and wake the waiting reader |
| [`xTaskCheckForTimeOut`](#xtaskcheckfortimeout) | 0x0C044378 | FreeRTOS: test whether a blocking timeout expired and adjust the remaining ticks |
| [`xTaskCreateStatic`](#xtaskcreatestatic) | 0x0C043CFC | FreeRTOS xTaskCreateStatic: initialise a caller-supplied TCB and stack and make the task ready |
| [`xTaskGenericNotify`](#xtaskgenericnotify) | 0x0C044870 | FreeRTOS: send a task notification from task context and unblock the target |
| [`xTaskGenericNotifyFromISR`](#xtaskgenericnotifyfromisr) | 0x0C044914 | FreeRTOS: send a task notification from an ISR and flag a higher-priority wake-up |
| [`xTaskGetCurrentTaskHandle`](#xtaskgetcurrenttaskhandle) | 0x0C04462C | FreeRTOS: return pxCurrentTCB |
| [`xTaskGetSchedulerState`](#xtaskgetschedulerstate) | 0x0C044638 | FreeRTOS: report scheduler not-started / running / suspended |
| [`xTaskGetTickCount`](#xtaskgettickcount) | 0x0C043F1C | FreeRTOS: return the current tick count |
| [`xTaskIncrementTick`](#xtaskincrementtick) | 0x0C043F48 | FreeRTOS: advance xTickCount, unblock expired delayed tasks and report whether to switch |
| [`xTaskNotifyStateClear`](#xtasknotifystateclear) | 0x0C0449FC | FreeRTOS: clear a pending notification state of a task (or the current task) |
| [`xTaskNotifyWait`](#xtasknotifywait) | 0x0C0447E8 | FreeRTOS: wait for a task notification, clearing bits on entry and exit |
| [`xTaskPriorityDisinherit`](#xtaskprioritydisinherit) | 0x0C0446E4 | FreeRTOS: drop an inherited priority when the last held mutex is released |
| [`xTaskPriorityInherit`](#xtaskpriorityinherit) | 0x0C044658 | FreeRTOS: raise a mutex holder's priority to that of the current task |
| [`xTaskRemoveFromEventList`](#xtaskremovefromeventlist) | 0x0C044264 | FreeRTOS: wake the highest-priority task blocked on an event list |
| [`xTaskResumeAll`](#xtaskresumeall) | 0x0C0440AC | FreeRTOS: resume the scheduler, drain the pending-ready list and replay pended ticks |
| [`xTimerCreateTimerTask`](#xtimercreatetimertask) | 0x0C044C2C | Create the 'Tmr Svc' FreeRTOS timer daemon task (static, depth 0x400, priority 5) |
| [`xTimerGenericCommand`](#xtimergenericcommand) | 0x0C044D90 | FreeRTOS xTimerGenericCommand: post a command to the timer daemon queue from task or ISR context |

## app_noop_hook_0c0427f0

**Empty function (single return), never called directly**

Contains only a return instruction. It has no direct callers, so it is an unused weak-default or an indirect hook/callback slot (possibly a FreeRTOS vApplicationIdleHook/vApplicationTickHook style stub).

- Addresses by version: 219: 0x0C0427F0
- Confidence: high

## ble_bt_stack_task_create

**Create the 'bt stack' RTOS task with entry 0x0C05B678 and a 1 KiB stack**

Creates the task named 'bt stack' with entry point 0x0C05B678, stack size 0x400 (1024), argument 0 and priority 2 through the RTOS wrapper 0x0C043CFC. The task handle is written to 0x20016044 and a second output object is written to 0x20004B38.

**Notes:** The argument order (stack size, argument, priority) is inferred from the call, and the purpose of the object at 0x20004B38 is unknown.

- Addresses by version: 219: 0x0C05B6CC
- Called by: `ble_219_0c0592a4`
- Calls: `xTaskCreateStatic`
- Confidence: medium

## ble_evt_clear_index_bit

**Clear the event bit that ble_evt_set_index_bit sets, via xEventGroupClearBits**

Uses the same index and selector mapping as ble_evt_set_index_bit and clears that bit in the event group at 0x2000F6D4 with FUN_0C042900, which is xEventGroupClearBits per its annotation. It returns immediately when the mask is zero. Callers are at 0x0C0422D4, 0x0C0424D8 and 0x0C04264C, which presumably consume a readiness event.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | descriptor index (descriptor number minus 3) |
| `param_2` | `u32` | selector: bit 0 set means read readiness, clear means write readiness |

- Addresses by version: 219: 0x0C048298
- Called by: `ble_ring_poll_status`, `ble_219_0c0424d8`, `ble_219_0c04264c`
- Calls: `xEventGroupClearBits`
- Confidence: medium

## ble_evt_read_bits

**Return the whole BLE event group value when the index bit is valid, else 0**

Returns 0 when the event group handle at 0x2000F6D4 is NULL or when the index's mask is zero. Otherwise it returns the result of FUN_0C042988 on the group (a one-argument call, presumed xEventGroupGetBits), which is the full group value and not only the requested bit, so callers must mask the result. Callers are at 0x0C04533C, 0x0C0462C4, 0x0C046380 and 0x0C0467B8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | descriptor index (descriptor number minus 3) |
| `param_2` | `u32` | selector, as in ble_evt_set_index_bit |

**Returns** `u32`: whole event group value, or 0

- Addresses by version: 219: 0x0C0482B8
- Called by: `ble_219_0c04533c`, `ble_219_0c0462c4`, `ble_219_0c046380`, `ble_219_0c0467b8`
- Calls: `rtos_timer_pend_fixed_callback_from_isr`
- Confidence: medium

## ble_evt_set_index_bit

**Set event bit 2*index + (selector & 1) in the BLE event group at 0x2000F6D4**

Maps an index and a selector to one bit of the event group at 0x2000F6D4: bit = 2*index + (selector & 1), with mask = 1 << bit. A mask of zero (bit 32 or more) skips the call. Otherwise it calls FUN_0C04291C with the group and the mask, presumed to be xEventGroupSetBits and the counterpart of the xEventGroupClearBits used by ble_evt_clear_index_bit. The even/odd layout is the one ble_fd_select uses: write readiness on the even bit and read readiness on the odd bit of descriptor index fd-3. Callers are at 0x0C0462C4 and 0x0C046380.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | descriptor index (descriptor number minus 3) |
| `param_2` | `u32` | selector: bit 0 set means read readiness, clear means write readiness |

- Addresses by version: 219: 0x0C048278
- Called by: `ble_219_0c0462c4`, `ble_219_0c046380`
- Calls: `xEventGroupSetBits`
- Confidence: medium

## ble_sched_check_and_pend_pendsv

**Request a PendSV exception when the scheduler object reports pending work**

Calls the status query at 0x0C042988 on the scheduler object at DAT_20017184 with flag 1 and a local out-word. If the out-word comes back non-zero it writes 0x10000000 to SCB->ICSR (0xE000ED04), the PENDSVSET bit, so the RTOS context switch runs once no higher-priority exception is active. It has no effect when the out-word is zero and does not clear any pending state itself. It has no direct callers in the packet, so it is reached through an indirect call or a table.

**Notes:** The status routine 0x0C042988 and the object type of DAT_20017184 are not described yet, so the meaning of the out-word is inferred from the PendSV write.

- Addresses by version: 219: 0x0C05D0C4
- Peripheral registers: `0xe000ed04` (W)
- Calls: `rtos_timer_pend_fixed_callback_from_isr`
- Confidence: medium

## ble_sched_signal_event

**Signal event 1 on the BLE scheduler object at 0x20017184**

Thin wrapper that calls the event-set primitive at 0x0C04291C with the object pointer DAT_20017184 and event number 1. It is the same signal that ble_xfer_pump_chunk_and_notify issues after moving a chunk, so it is used to wake the BLE task when work becomes ready. Its caller 0x0C05AE14 is not described yet.

- Addresses by version: 219: 0x0C05D494
- Called by: `ble_msg_enqueue`
- Calls: `xEventGroupSetBits`
- Confidence: medium

## ble_signal_worker_event

**Signal the BLE worker event handle held in the global at 0x20014564**

A one-line trampoline. It calls the RTOS wrapper 0x0C04291C with the event or semaphore handle stored at 0x20014564 and the value 1, which wakes the waiting worker.

**Notes:** The handle at 0x20014564 is set elsewhere. Callers are not named in this packet (entry point, callback or indirect call).

- Addresses by version: 219: 0x0C059938
- Calls: `xEventGroupSetBits`
- Confidence: high

## ble_stack_lock_give

**Release the shared BLE stack mutex taken by ble_stack_lock_take**

Gives the mutex at handle 0x2000F4C0 through FUN_0C042DF4 when the handle is non-NULL and xTaskGetSchedulerState is not 0 (not suspended), mirroring the take. It does nothing when the mutex was never created or the scheduler is suspended, so a scheduler suspension between take and give leaves the mutex held; that case is not handled.

- Addresses by version: 219: 0x0C046EC0
- Called by: `ble_219_0c070f40`, `ble_219_0c070fd8`, `ble_219_0c071080`
- Calls: `xQueueGiveMutexRecursive`, `xTaskGetSchedulerState`
- Confidence: medium

## ble_stack_lock_take

**Take the shared BLE stack mutex, creating it on first use while the scheduler runs**

Creates the mutex lazily: if the handle at 0x2000F4C0 is NULL, FUN_0C042D80 is called with type 4 (presumed FreeRTOS recursive mutex) and the static 80-byte buffer at 0x2000F470, and the function returns if creation fails. Otherwise, when xTaskGetSchedulerState reports anything but 0 (suspended), the mutex is taken with an infinite timeout through FUN_0C0431F8. Nothing is taken while the scheduler is suspended, and ble_stack_lock_give applies the same test on release. Callers at 0x0C070F40, 0x0C070FD8 and 0x0C071080 use it around shared BLE stack code.

**Notes:** The type code 4 and the FUN_0C0431F8 take are inferred from the other uses in this packet (for example the streaming buffer in ble_pktq_enqueue).

- Addresses by version: 219: 0x0C046E88
- Called by: `ble_219_0c070f40`, `ble_219_0c070fd8`, `ble_219_0c071080`
- Calls: `prvInitialiseMutex`, `xQueueTakeMutexRecursive`, `xTaskGetSchedulerState`
- Confidence: medium

## pcTaskGetName

**FreeRTOS: return pointer to a task's name string**

If param_1 is non-NULL returns param_1 + 0x34, else uses the current TCB (DAT_2000cb8c) + 0x34. Offset 0x34 is pcTaskName in this build's TCB_t layout (pxTopOfStack 0, state item 4, event item 0x18, uxPriority 0x2c, pxStack 0x30). Caller ble_219_0c036328.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TaskHandle_t or NULL for the calling task |

**Returns** `ptr`: pointer to the NUL-terminated task name

- Addresses by version: 219: 0x0C043F34
- Called by: `ble_219_0c036328`
- Confidence: high

## posix_event_2000f65c_init

**Static constructor: initialise the RTOS event object at 0x2000F660 and store its handle in 0x2000F65C**

Calls ble_219_0c04281c on the static 32-byte object at 0x2000F660 (word 0 = 0, a self-linked wait list at +4..+0x10 initialised by ble_219_0c0429a4, byte +0x1c = 1 'initialised') and stores the returned pointer in DAT_2000f65c. The address 0x0C047F71 is the first of two consecutive function pointers at 0x0C073CD8 (next: ble_219_0c048260), i.e. an .init_array-style constructor table run during startup; there are no direct callers. The twin ble_219_0c048260 creates the event object that the POSIX select() emulation waits on, so this object belongs to the same /dev file-descriptor layer, but nothing in the image reads DAT_2000f65c.

**Notes:** Exact object type (event flags vs. semaphore) inferred from the sibling's use in select(); the constructor-table mechanism is inferred from the pointer pair at 0x0C073CD8.

- Addresses by version: 219: 0x0C047F70
- Calls: `xEventGroupCreateStatic`
- Confidence: medium

## posix_select_event_init

**Static constructor: initialise the RTOS event object that the fd-layer select() waits on**

Calls ble_219_0c04281c on the static object at 0x2000F790 (word 0 = 0, self-linked wait list at +4, byte +0x1c = 1) and stores the returned handle in DAT_2000f6d4. DAT_2000f6d4 is later passed to the blocking wait ble_219_0c042858(handle, mask, 0, 0, timeout_ms) by the select() implementation ble_219_0c04885c, which polls the /dev file-descriptor table DAT_2000f6d8 (fds 3..48). Address 0x0C048261 is the second pointer of the constructor table at 0x0C073CD8 (after ble_219_0c047f70); no direct callers.

**Notes:** The object is treated as event flags because select() waits on it with a bit mask.

- Addresses by version: 219: 0x0C048260
- Calls: `xEventGroupCreateStatic`
- Confidence: medium

## prvAddCurrentTaskToDelayedList

**FreeRTOS: move the running task to the delayed, overflow-delayed or suspended list**

tasks.c prvAddCurrentTaskToDelayedList(xTicksToWait, xCanBlockIndefinitely). Clears ucDelayAborted (TCB+0x5e) of pxCurrentTCB (DAT_2000cb8c) and unlinks its xStateListItem (TCB+4) from the ready list with uxListRemove. If xTicksToWait == portMAX_DELAY (0xffffffff) and blocking indefinitely is allowed, the item is appended to xSuspendedTaskList (0x2000cc78). Otherwise the wake time xTickCount (DAT_2000cca0) + xTicksToWait is stored as the item value; when that addition wraps the item goes into pxOverflowDelayedTaskList (DAT_2000cb94) via the sorted vListInsert, else into pxDelayedTaskList (DAT_2000cb90) and xNextTaskUnblockTime (DAT_2000cc58) is lowered to the wake time if earlier. The caller must hold the scheduler suspended or be in a critical section. Callers: vTaskDelay (0x0c0441a8), vTaskPlaceOnEventList, vTaskPlaceOnUnorderedEventList, vTaskPlaceOnEventListRestricted and xTaskNotifyWait.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | xTicksToWait (ticks), 0xffffffff = portMAX_DELAY |
| `param_2` | `bool` | xCanBlockIndefinitely |

- Addresses by version: 219: 0x0C043A7C
- Called by: `vTaskDelay`, `vTaskPlaceOnEventList`, `vTaskPlaceOnUnorderedEventList`, `vTaskPlaceOnEventListRestricted`, `xTaskNotifyWait`
- Calls: `vListInsertEnd`, `vListInsert`, `uxListRemove`
- Confidence: high

## prvAddNewTaskToReadyList

**FreeRTOS: register a freshly created TCB with the scheduler and put it on its ready list**

tasks.c prvAddNewTaskToReadyList(pxNewTCB). Inside vPortEnterCritical/vPortExitCritical (0x0c03f640/0x0c03f65c): increments uxCurrentNumberOfTasks (DAT_2000cc14); if this is the very first task it also runs prvInitialiseTaskLists inline, calling vListInitialise on the six ready lists pxReadyTasksLists[0..5] at 0x2000cb98 (20 bytes each, up to 0x2000cc10, so configMAX_PRIORITIES = 6), xDelayedTaskList1 (0x2000cc2c), xDelayedTaskList2 (0x2000cc40), xPendingReadyList (0x2000cc60), xTasksWaitingTermination (0x2000cc8c) and xSuspendedTaskList (0x2000cc78), and sets pxDelayedTaskList (DAT_2000cb90) / pxOverflowDelayedTaskList (DAT_2000cb94). pxCurrentTCB (DAT_2000cb8c) becomes the new task when it is NULL, or when the scheduler is not yet running (xSchedulerRunning DAT_2000cc74 == 0) and the new priority (TCB+0x2c) is >= the current one. uxTaskNumber (DAT_2000cc24) is incremented and stored as uxTCBNumber (TCB+0x44); uxTopReadyPriority (DAT_2000cc28) is raised if needed and the xStateListItem (TCB+4) is appended to pxReadyTasksLists[priority] with vListInsertEnd. If the scheduler is running and the new task has a strictly higher priority than pxCurrentTCB, rtos_pendsv_trigger requests a context switch. Called from xTaskCreateStatic / xTaskCreate (0x0c043cfc, 0x0c043d3c, 0x0c043e70).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TCB_t* of the new task |

- Addresses by version: 219: 0x0C043978
- Called by: `xTaskCreateStatic`, `ble_219_0c043d3c`, `ble_219_0c043e70`
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `vListInitialise`, `vListInsertEnd`
- Confidence: high

## prvCheckForValidListAndQueue

**Create the timer lists and the timer command queue (8 x 16 bytes) once, under a critical section**

Upstream prvCheckForValidListAndQueue. Inside a critical section, if the timer command queue handle DAT_2000DE20 is still NULL, it initialises the timer lists at 0x2000DD90 and 0x2000DDA4 and points the current and overflow timer list pointers (DAT_2000CCA8, DAT_2000CCAC) at them. It also initialises the third list at 0x2000DDB8, which ble_219_0c044de8 uses. Then it creates the timer queue with xQueueGenericCreateStatic (0x0C042BA0) as 8 entries of 16 bytes, storage at 0x2000DD10 and Queue_t at 0x2000DDD0. Called from the timer task creation path (ble_219_0c044c2c) and from ble_219_0c044c7c.

- Addresses by version: 219: 0x0C044AA4
- Called by: `xTimerCreateTimerTask`, `ble_219_0c044c7c`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `vListInitialise`, `prvInitialiseNewQueue`
- Confidence: high

## prvCopyDataToQueue

**FreeRTOS queue.c: copy an item into the queue at back/front/overwrite position, or release a mutex**

Queue_t layout: pcHead +0, pcTail +4, pcWriteTo +8, pcReadFrom +0xC, uxMessagesWaiting +0x38, uxLength +0x3C, uxItemSize +0x40. If uxItemSize == 0 and pcHead == NULL (mutex) it calls xTaskPriorityDisinherit (0x0c0446e4) on the holder stored in +4 (pxMutexHolder) and clears it, returning that result. For xPosition == queueSEND_TO_BACK (0): memcpy(pcWriteTo, item, uxItemSize), advance pcWriteTo and wrap to pcHead when it reaches pcTail. Otherwise (queueSEND_TO_FRONT 1 / queueOVERWRITE 2): memcpy(pcReadFrom, item, uxItemSize), move pcReadFrom back one item wrapping to pcTail - uxItemSize; for queueOVERWRITE the message count is first decremented if non-zero so the net count becomes max(1, count). Finally uxMessagesWaiting is incremented. Must be called with the critical section held. Callers: xQueueGenericSend (0x0c042c8c) and xQueueGenericSendFromISR (0x0c042eb4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Queue_t *pxQueue |
| `param_2` | `ptr` | pvItemToQueue |
| `param_3` | `s32` | xPosition: 0 back, 1 front, 2 overwrite |

**Returns** `u32`: pdFALSE, or xTaskPriorityDisinherit's result for a mutex give

**Notes:** Field offsets correspond to FreeRTOS 10.x with configUSE_TRACE_FACILITY and without queue sets.

- Addresses by version: 219: 0x0C042A3C
- Called by: `xQueueGenericSend`, `xQueueGenericSendFromISR`
- Calls: `xTaskPriorityDisinherit`, `memcpy`
- Confidence: high

## prvInitialiseMutex

**Initialise a static one-slot, zero-item-size queue as a mutex or semaphore and give its token**

Initialises a caller-supplied static Queue_t as a one-entry, zero-item-size queue: uxLength 1, uxItemSize 0, both lock counters set to unlocked (-1), both wait lists initialised with vListInitialise, the holder and read pointer cleared and the type byte set from param_1. It finishes by calling xQueueGenericSend(queue, NULL, 0, back) so that the new mutex or semaphore starts with its token available. Returns the queue handle, or NULL when the storage pointer is NULL.

| Parameter | Type | Description |
|---|---|---|
| `queueType` | `u8` | queue type code stored in the queue (1 mutex, 3 binary semaphore) |
| `pxStaticQueue` | `ptr` | static Queue_t storage |

**Returns** `ptr`: the queue handle, or NULL

**Notes:** Matches upstream prvInitialiseMutex and the static create path, but the decompile merges the two. The name is therefore a best match and is not confirmed against the source.

- Addresses by version: 219: 0x0C042D80
- Called by: `ble_219_0c0297b0`, `ble_219_0c02a478`, `ble_219_0c02dea8`, `ble_219_0c02e420`, `ble_219_0c035d30`, `ble_stack_lock_take`, `ble_219_0c048138`, `ble_219_0c048204`, `ble_219_0c0482e4`, `ble_fd_find_next_open`, `ble_219_0c04855c`, `ble_pktq_init` ...
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `vListInitialise`, `xQueueGenericSend`
- Confidence: medium

## prvInitialiseNewQueue

**FreeRTOS queue.c: fill a static Queue_t (length, item size, storage, type) and reset it**

If pxNewQueue is non-NULL: for uxItemSize == 0 the storage pointer is set to the queue structure itself (mutex/semaphore convention), uxLength (+0x3C) = param_1, uxItemSize (+0x40) = param_2, pcHead (+0) = storage, ucStaticallyAllocated (+0x46) = pdTRUE, then the body of xQueueGenericReset(xNewQueue = pdTRUE) is inlined inside taskENTER/EXIT_CRITICAL (0x0c03f640/0x0c03f65c): pcTail, pcWriteTo, pcReadFrom computed from head/length/item size, uxMessagesWaiting = 0, both locks = 0xFF, vListInitialise on xTasksWaitingToSend (+0x10) and xTasksWaitingToReceive (+0x24). Finally ucQueueType (+0x4C, trace facility layout) = param_5. Returns pxNewQueue. Called from the queue/semaphore creators 0x0c02d724, 0x0c02e420, 0x0c0355c8, 0x0c044aa4 and 0x0c045250, which supply static buffers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | uxQueueLength |
| `param_2` | `u32` | uxItemSize (0 for semaphores/mutexes) |
| `param_3` | `ptr` | pucQueueStorage (ignored when item size is 0) |
| `param_4` | `ptr` | Queue_t *pxNewQueue (StaticQueue_t storage) |
| `param_5` | `u8` | ucQueueType (queueQUEUE_TYPE_*) |

**Returns** `ptr`: QueueHandle_t = param_4

**Notes:** Parameter order differs from stock FreeRTOS (queue pointer before type) and the static flag is set here rather than in xQueueGenericCreateStatic, so this is a merged/customised version.

- Addresses by version: 219: 0x0C042BA0
- Called by: `ble_219_0c02d724`, `ble_219_0c02e420`, `ble_219_0c0355c8`, `prvCheckForValidListAndQueue`, `ble_irq_binary_sem_init`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `vListInitialise`
- Confidence: medium

## prvInitialiseNewTask

**FreeRTOS: fill a TCB, paint the stack and build the initial context for a new task**

tasks.c prvInitialiseNewTask(pxTaskCode, pcName, ulStackDepth, pvParameters, uxPriority, pxCreatedTask, pxNewTCB) without the MPU xRegions argument. Fills the stack (TCB+0x30 = pxStack) with tskSTACK_FILL_BYTE 0xa5 over ulStackDepth*4 bytes, copies up to 16 characters of the name into pcTaskName (TCB+0x34) and forces pcTaskName[15] = 0, clamps the priority to configMAX_PRIORITIES-1 = 5 and stores it in uxPriority (+0x2c) and uxBasePriority (+0x4c), zeroes uxMutexesHeld (+0x50), ulRunTimeCounter (+0x54), ulNotifiedValue (+0x58), ucNotifyState (+0x5c) and ucDelayAborted (+0x5e). Both list items are initialised with vListInitialiseItem: xStateListItem (+4, owner = TCB) and xEventListItem (+0x18, owner = TCB, value = 6 - priority so that higher priorities sort first). The top of stack is pxStack + depth*4 - 4 rounded down to 8 bytes; pxTopOfStack (+0) receives rtos_task_stack_init(top, pxStack (stack limit for PSPLIM), pxTaskCode, pvParameters). If pxCreatedTask is non-NULL the TCB pointer is returned through it. Called from the task-create routines 0x0c043cfc, 0x0c043d3c, 0x0c043e70.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pxTaskCode entry function |
| `param_2` | `ptr` | pcName, up to 16 chars |
| `param_3` | `u32` | ulStackDepth in 32-bit words |
| `param_4` | `ptr` | pvParameters passed in r0 to the task |
| `param_5` | `u32` | uxPriority 0..5 (clamped) |
| `param_6` | `ptr` | TaskHandle_t* pxCreatedTask output (may be NULL) |
| `param_7` | `ptr` | TCB_t* pxNewTCB to initialise (pxStack already set at +0x30) |

- Addresses by version: 219: 0x0C043BA8
- Called by: `xTaskCreateStatic`, `ble_219_0c043d3c`, `ble_219_0c043e70`
- Calls: `rtos_task_stack_init`, `vListInitialiseItem`, `memset`
- Confidence: high

## prvInsertTimerInActiveList

**FreeRTOS timers: queue a software timer in the current or overflow timer list**

timers.c prvInsertTimerInActiveList(pxTimer, xNextExpiryTime, xTimeNow, xCommandTime). Timer_t layout: +4 xTimerListItem (xItemValue +4, pvOwner +0x10, pvContainer +0x14), +0x18 xTimerPeriodInTicks. Sets the item owner and value = expiry time. If the expiry is still in the future and the command was not issued after a tick wrap, the item is inserted (sorted) into pxCurrentTimerList (DAT_2000cca8); if the expiry already wrapped but less than one period has elapsed since the command, it goes into pxOverflowTimerList (DAT_2000ccac). In both insert cases, if the item currently sits in the third list at 0x2000ddb8 (a BES addition to the two active lists initialised in 0x0c044aa4) it is first unlinked with uxListRemove. Returns 1 (xProcessTimerNow) when the timer must be processed immediately instead. Called by the timer command processor 0x0c044ee8 (prvProcessReceivedCommands).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Timer_t* timer |
| `param_2` | `u32` | xNextExpiryTime (ticks) |
| `param_3` | `u32` | xTimeNow (ticks) |
| `param_4` | `u32` | xCommandTime (ticks when the command was queued) |

**Returns** `bool`: 1 if the timer has already expired and must be processed now, 0 if queued

**Notes:** The uxListRemove-when-in-list-0x2000ddb8 check is not in stock FreeRTOS; purpose of that list is unknown.

- Addresses by version: 219: 0x0C044BB0
- Called by: `ble_219_0c044ee8`
- Calls: `vListInsert`, `uxListRemove`
- Confidence: high

## prvIsQueueEmpty

**FreeRTOS queue: true when no messages are waiting**

Returns (Queue_t.uxMessagesWaiting at offset 0x38) == 0. This is the body of prvIsQueueEmpty / the check used by xQueueIsQueueEmptyFromISR; callers do not necessarily hold a critical section.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Queue_t* queue |

**Returns** `bool`: true if the queue holds no items

- Addresses by version: 219: 0x0C043364
- Called by: `ble_ring_poll_status`, `ble_219_0c04264c`, `ble_219_0c0467b8`
- Confidence: high

## prvIsQueueFull

**FreeRTOS queue: true when uxMessagesWaiting equals uxLength**

Returns (Queue_t.uxLength at 0x3c) == (Queue_t.uxMessagesWaiting at 0x38), i.e. the queue has no free slots. Equivalent to prvIsQueueFull / xQueueIsQueueFullFromISR.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Queue_t* queue |

**Returns** `bool`: true if the queue is full

- Addresses by version: 219: 0x0C043370
- Called by: `ble_219_0c0424d8`
- Confidence: high

## prvListTasksWithinSingleList

**FreeRTOS prvListTasksWithinSingleList: append a TaskStatus_t for each task of one list**

Upstream prvListTasksWithinSingleList(pxTaskStatusArray, pxList, eState). It walks the list items from the first entry up to the end marker. For each task it calls vTaskGetInfo (0x0C044400) into the next 36-byte slot, with the given state and no stack scan. Returns the number of entries written. Used by uxTaskGetSystemState for the ready, delayed, overflow-delayed, terminated and suspended lists.

| Parameter | Type | Description |
|---|---|---|
| `pxTaskStatusArray` | `ptr` | output array of TaskStatus_t |
| `pxList` | `ptr` | task list to walk |
| `eState` | `s32` | state reported for every task in the list |

**Returns** `s32`: number of entries written

- Addresses by version: 219: 0x0C0444F4
- Called by: `uxTaskGetSystemState`
- Calls: `vTaskGetInfo`
- Confidence: high

## prvReadBytesFromBuffer

**FreeRTOS stream_buffer.c: copy min(xMaxCount, xBytesAvailable) bytes out of the circular buffer at xTail**

xCount = min(xMaxCount, xBytesAvailable); returns 0 immediately if that is 0. Otherwise copies min(xLength - xTail, xCount) bytes from pucBuffer (+0x18) + xTail (+0) to pucData with memcpy, then the remaining bytes from the start of pucBuffer, advances xTail by xCount wrapping modulo xLength (+8) and returns xCount. Called from the receive path prvReadMessageFromBuffer/xStreamBufferReceive at 0x0c0436f8. Partner of prvWriteBytesToBuffer (0x0c0433d0).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | StreamBuffer_t *pxStreamBuffer |
| `param_2` | `ptr` | uint8_t *pucData destination |
| `param_3` | `u32` | xMaxCount |
| `param_4` | `u32` | xBytesAvailable in the buffer |

**Returns** `u32`: bytes copied

- Addresses by version: 219: 0x0C043414
- Called by: `xStreamBufferReceive`
- Calls: `memcpy`
- Confidence: high

## prvSwitchTimerLists

**Run the timers in the current list and swap the current and overflow timer lists**

Used when the tick count wraps (upstream prvSwitchTimerLists). While the current timer list is non-empty it takes the head timer, removes it with uxListRemove and moves it onto the internal list at 0x2000DDB8 with vListInsert. It reads a 64-bit hardware counter before and after the timer's callback (the pointer at +0x24) and accumulates the elapsed time, scaled by 1,000,000, into a 64-bit per-timer field at +0x30/+0x34. Auto-reload timers (status word at +0x1C equal to 1) get the next expiry (expiry plus period at +0x18); if that does not wrap they are reinserted into the current list, otherwise they are restarted with xTimerGenericCommand. Finally the current and overflow list pointers at DAT_2000CCA8 and DAT_2000CCAC are swapped.

**Notes:** The 64-bit arithmetic and the time source behind 0x0C071A70 are hard to read in the decompile, so the elapsed-time accounting is the least certain part. The list swap and the auto-reload branch follow upstream closely.

- Addresses by version: 219: 0x0C044DE8
- Called by: `ble_219_0c044ee8`
- Calls: `vListInsert`, `uxListRemove`, `xTimerGenericCommand`, `_gettimeofday_r`
- Confidence: medium

## prvUnlockQueue

**FreeRTOS queue.c: unlock a queue, waking tasks blocked on receive/send for each pending lock count**

Two critical sections (taskENTER/EXIT_CRITICAL at 0x0c03f640/0x0c03f65c). First: while cTxLock (byte +0x45) > 0 and xTasksWaitingToReceive (List_t at +0x24) is non-empty, xTaskRemoveFromEventList (0x0c044264) wakes one receiver and vTaskMissedYield() is called if that task has higher priority; the counter is decremented each pass; then cTxLock = queueUNLOCKED (0xFF). Second: the same for cRxLock (byte +0x44) with xTasksWaitingToSend (List_t at +0x10). Called after a queue operation with the scheduler suspended, from xQueueGenericSend (0x0c042c8c) and the receive/peek/semaphore-take functions 0x0c042fa4, 0x0c0430a8, 0x0c043224, 0x0c043380.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Queue_t *pxQueue |

- Addresses by version: 219: 0x0C042AAC
- Called by: `xQueueGenericSend`, `xQueueReceive`, `xQueueSemaphoreTake`, `xQueuePeek`, `vQueueWaitForMessageRestricted`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `xTaskRemoveFromEventList`, `vTaskMissedYield`
- Confidence: high

## prvWriteBytesToBuffer

**FreeRTOS stream_buffer.c: copy xCount bytes into the circular buffer at xHead with wrap-around**

StreamBuffer_t layout: xTail +0, xHead +4, xLength +8, xTriggerLevelBytes +0xC, xTaskWaitingToReceive +0x10, xTaskWaitingToSend +0x14, pucBuffer +0x18, ucFlags +0x1C, uxStreamBufferNumber +0x20 (0x24 bytes). Copies min(xLength - xHead, xCount) bytes with memcpy to pucBuffer + xHead, then the remainder (if any) to the start of pucBuffer, advances xHead by xCount wrapping modulo xLength and returns xCount. No space check: callers (xStreamBufferSend at 0x0c043554 and the ISR variant 0x0c043658) have already verified the free space.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | StreamBuffer_t *pxStreamBuffer |
| `param_2` | `ptr` | const uint8_t *pucData |
| `param_3` | `u32` | xCount bytes to write |

**Returns** `u32`: xCount

- Addresses by version: 219: 0x0C0433D0
- Called by: `xStreamBufferSend`, `xStreamBufferSendFromISR`
- Calls: `memcpy`
- Confidence: high

## pvTaskIncrementMutexHeldCount

**FreeRTOS: increment the running task's mutex-held counter**

If pxCurrentTCB (DAT_2000cb8c) is non-NULL, increments the counter at TCB+0x50 (uxMutexesHeld) and returns the TCB pointer. Called by the semaphore-take path (ble_219_0c0430a8) after acquiring a mutex so priority-inheritance bookkeeping stays valid.

**Returns** `ptr`: current TCB (may be NULL before scheduler start)

- Addresses by version: 219: 0x0C0447D0
- Called by: `xQueueSemaphoreTake`
- Confidence: high

## rtos_enter_critical

**Raise BASEPRI to 0x40 and return the previous value (start of critical section)**

If in a privileged mode, reads the current BASEPRI, then sets BASEPRI to 0x40 (masking interrupts with priority value >= 0x40 while keeping higher-priority ones active), followed by DSB/ISB. Returns a 64-bit value whose low word is the previous BASEPRI (0 if unprivileged) and whose high word is 0x40; callers pass the low word to rtos_exit_critical. Used throughout RTOS code and the controller (callers include 0x0c03f640, 0x0c042eb4, 0x0c043658, 0x0c044914).

**Returns** `u64`: low 32 bits = previous BASEPRI, high 32 bits = new BASEPRI (0x40)

- Addresses by version: 219: 0x0C03F874
- Called by: `vPortEnterCritical`, `SysTick_Handler`, `ble_219_0c041d28`, `xQueueGenericSendFromISR`, `xQueueGiveFromISR`, `xStreamBufferSendFromISR`, `stream_buffer_consume_tail`, `stream_buffer_commit_head`, `ble_219_0c043e70`, `xTaskGenericNotifyFromISR`
- Confidence: high

## rtos_exit_critical

**Restore BASEPRI to a saved value (end of critical section)**

If privileged, writes param_1 into BASEPRI, then DSB and ISB. Counterpart of rtos_enter_critical; param_1 is the previous BASEPRI it returned. Called by the RTOS primitives after their critical sections.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | BASEPRI value to restore (as returned by rtos_enter_critical) |

- Addresses by version: 219: 0x0C03F88C
- Called by: `vPortExitCritical`, `SysTick_Handler`, `xQueueGenericSendFromISR`, `xQueueGiveFromISR`, `xStreamBufferSendFromISR`, `stream_buffer_consume_tail`, `stream_buffer_commit_head`, `xTaskGenericNotifyFromISR`
- Confidence: high

## rtos_mutex_give_checked

**Release a non-recursive mutex the caller holds: clear the recursion count and send the token**

If the caller (xTaskGetCurrentTaskHandle) is the holder at +4, sets the recursion count at +0xC to zero and posts the token back with xQueueGenericSend (ble_219_0c042c8c) with a NULL item and zero timeout, then returns 1. If the caller is not the holder it returns 0 and does nothing. This is the holder-checked give used for a plain, non-recursive mutex.

| Parameter | Type | Description |
|---|---|---|
| `xMutex` | `ptr` | mutex handle |

**Returns** `s32`: 1 when released, 0 when the caller was not the holder

**Notes:** Upstream FreeRTOS does not check the holder in xSemaphoreGive, so this name describes this build's variant.

- Addresses by version: 219: 0x0C042E20
- Called by: `ble_219_0c048380`
- Calls: `xQueueGenericSend`, `xTaskGetCurrentTaskHandle`
- Confidence: high

## rtos_pendsv_trigger

**Pend the PendSV exception to request a context switch**

Writes 0x10000000 (PENDSVSET, bit 28) to SCB->ICSR at 0xE000ED04, then DSB and ISB. This makes the PendSV handler run as soon as no higher-priority exception is active. Called from many RTOS primitives (semaphore/mutex/queue/timer/delay) in the 0x0c0428xx..0x0c0448xx range after a task becomes ready.

- Addresses by version: 219: 0x0C03F628
- Peripheral registers: `0xe000ed04` (W)
- Called by: `xEventGroupWaitBits`, `xQueueGenericReset`, `xQueueGenericSend`, `xQueueReceive`, `xQueueSemaphoreTake`, `xQueuePeek`, `prvAddNewTaskToReadyList`, `ble_219_0c043da0`, `xTaskResumeAll`, `vTaskDelay`, `xTaskNotifyWait`, `xTaskGenericNotify` ...
- Confidence: high

## rtos_pool_node_alloc_init

**Pop a node from a free list under a BASEPRI critical section and initialise it**

Enters a critical section (raises BASEPRI to 0x40 if running privileged; when not already nested it records the caller address 0xc04212a and LR in DAT_20003d70/DAT_20003d74 as a lock-owner trace and clears DAT_20003d70 to -1 on exit). Takes the head of the singly linked free list DAT_2000c720 (next pointer at node+4) and advances the head. If a node was obtained, checks that its state byte (offset 0) is 0 - otherwise it spins forever as an assertion - then stores param_1 at +0xc and param_2 at +0x10, zeroes the 32-bit field at +4..+7 and marks the node in use (state byte = 1). Returns the node, or NULL if the pool was empty.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | value stored in node+0xc (callback/argument, unknown) |
| `param_2` | `u32` | value stored in node+0x10 |

**Returns** `ptr`: allocated node or NULL if the free list is empty

**Notes:** Node type unknown (looks like an RTOS control block / message / timer slot pool). Sole caller ble_219_0c03bb70.

- Addresses by version: 219: 0x0C04211C
- Called by: `ble_219_0c03bb70`
- Confidence: medium

## rtos_port_yield_from_isr

**Cortex-M: pend PendSV when param_1 is non-zero (portYIELD_FROM_ISR)**

If param_1 != 0 writes 0x10000000 (PENDSVSET, bit 28) to SCB->ICSR at 0xE000ED04, requesting a context switch at the next exception return. Implements the portYIELD_FROM_ISR(xHigherPriorityTaskWoken) macro as a function; caller ble_219_0c02feec.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | non-zero if a higher priority task was woken |

- Addresses by version: 219: 0x0C04583C
- Peripheral registers: `0xe000ed04` (W)
- Called by: `hal_gpio_irq_handler`
- Confidence: high

## rtos_run_time_counter_get

**Thunk to RAM patch 0x20000328: read the run-time-stats counter for FreeRTOS**

Single tail-call thunk into the patched RAM routine at 0x20000328 (via ble_ram_patch_thunk_20000328). The scheduler's vTaskSwitchContext (0x0c0441d4) uses its result as portGET_RUN_TIME_COUNTER_VALUE(): the delta to ulTotalRunTime (DAT_2000cc10) is accumulated into pxCurrentTCB->ulRunTimeCounter (TCB+0x54); the run-time-stats formatter 0x0c044544 also calls it. The underlying counter is most likely the BES hal_sys_timer_get() tick.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | forwarded to the patched routine (unused by callers) |

**Returns** `u32`: free-running time counter value

- Addresses by version: 219: 0x0C046290
- Called by: `ble_219_0c0441d4`, `uxTaskGetSystemState`
- Calls: `ble_ram_patch_thunk_20000328`
- Confidence: medium

## rtos_start_first_task

**Reset MSP from the vector table, enable interrupts and trigger SVC #2 to start the scheduler**

Reads VTOR (0xE000ED08), loads the first word of the vector table (initial MSP) into MSP if privileged, enables IRQ and FIQ (CPSIE i/f), executes DSB/ISB, then issues SVC 2. Control never returns: the SVC handler (0x0c03f910) switches to the first task on PSP. Called from the scheduler start routine 0x0c043e70.

- Addresses by version: 219: 0x0C03F850
- Peripheral registers: `0xe000ed08` (R)
- Called by: `ble_219_0c043e70`
- Confidence: high

## rtos_systick_sub_tick_ns

**Nanoseconds elapsed inside the current 1 ms SysTick period, +1 ms if the COUNTFLAG shows a wrap**

Reads SysTick LOAD and VAL, gets the reference clock frequency (Hz) from ble_ram_patch_thunk_20000554 and computes ((LOAD - VAL) * 1000000) / (freq / 1000), i.e. (LOAD - VAL) * 1e9 / freq nanoseconds (64-bit division, but the multiplication is 32-bit). It then reads CTRL and, if bit 16 (COUNTFLAG, the counter wrapped since the last read) is set, adds 1000000 ns (one tick). Used by the time-stamp helpers 0x0c03feac and 0x0c0400cc to combine the tick counter with a sub-tick fraction.

**Returns** `u32`: nanoseconds since the start of the current tick (0..~2,000,000)

**Notes:** Unit derived from the formula; the 32-bit multiply only avoids overflow if the reference clock is a few MHz or less (the SysTick CLKSOURCE bit is 0, so an external slow reference is plausible).

- Addresses by version: 219: 0x0C03F790
- Peripheral registers: `0xe000e010` (R), `0xe000e014` (R), `0xe000e018` (R)
- Called by: `clock_gettime`, `gettimeofday`
- Calls: `ble_ram_patch_thunk_20000554`
- Confidence: medium

## rtos_task_stack_init

**Build the initial context frame on a new task stack and return the new stack pointer**

Takes the stack top in param_1 and writes a fake exception frame below it: hardware-stacked part xPSR=0x01000000 at -4, PC=param_3 (task entry) at -8, LR=0x0c03f5e8 (task-exit/return stub) at -0xC, R12=0x12121212, R3..R1=0x03030303/0x02020202/0x01010101, R0=param_4 (task argument) at -0x20. Below it come software-saved R11..R4 filled with the debugging patterns 0x11111111..0x04040404, the EXC_RETURN value 0xFFFFFFFD (return to thread mode on PSP) at -0x44 and param_2 at -0x48 (the per-task stack limit saved with the context). Returns top - 0x48, the value stored as the task's saved SP. Called from the task-create routine 0x0c043ba8; matches the layout of CMSIS-RTOS RTX osRtxThreadStack init for Cortex-M33.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | top of the task stack (address of first byte above the stack) |
| `param_2` | `u32` | value stored as the saved stack limit (PSPLIM) |
| `param_3` | `u32` | task entry function address (initial PC) |
| `param_4` | `u32` | argument passed to the task in R0 |

**Returns** `ptr`: initial saved stack pointer (param_1 - 0x48)

**Notes:** Identity of param_2 as stack limit is inferred from SVC_Handler, which loads PSPLIM from the first word of the TCB.

- Addresses by version: 219: 0x0C03F6C4
- Called by: `prvInitialiseNewTask`
- Confidence: high

## rtos_timer_pend_fixed_callback_from_isr

**ISR-safe post of a fixed deferred callback with two arguments to the timer daemon queue**

Builds a 16-byte timer-daemon message on the stack: command id -2 (tmrCOMMAND_EXECUTE_CALLBACK_FROM_ISR), a constant callback address (thumb address 0x0C042984), the first argument and the second argument. It posts the message to the timer command queue in DAT_2000DE20 at the back with ble_219_0c042eb4 (xQueueGenericSendFromISR), passing the higher-priority-woken pointer through. The callback runs later in the timer service task. A fixed callback address makes this a specialised form of xTimerPendFunctionCallFromISR.

| Parameter | Type | Description |
|---|---|---|
| `pvParameter1` | `ptr` | first callback argument (pvParameter1) |
| `ulParameter2` | `u32` | second callback argument (ulParameter2) |
| `pxHigherPriorityTaskWoken` | `ptr` | pxHigherPriorityTaskWoken, may be NULL |

**Notes:** The code at 0x0C042984 that serves as the callback is not described here, so the callee's purpose is unknown.

- Addresses by version: 219: 0x0C042988
- Called by: `ble_evt_read_bits`, `ble_sched_check_and_pend_pendsv`
- Calls: `xQueueGenericSendFromISR`
- Confidence: medium

## stream_buffer_commit_head

**Advance a stream buffer's head by up to N free bytes and wake a receiver at the trigger level**

Clamps the requested count to the free space (length - 1 - stored), advances xHead with wrap-around, and when the stored byte count has reached the trigger level (+0x0C) notifies the task waiting to receive (xTaskWaitingToReceive, +0x10). Task context uses xTaskGenericNotify under scheduler suspension; ISR context uses rtos_enter_critical, xTaskGenericNotifyFromISR with pxHigherPriorityTaskWoken, and rtos_exit_critical. Returns the number of bytes committed. Internal helper of the stream buffer family.

| Parameter | Type | Description |
|---|---|---|
| `xStreamBuffer` | `ptr` | stream buffer |
| `uxBytes` | `u32` | bytes written into the free space |
| `fromISR` | `bool` | true for interrupt context |
| `pxHigherPriorityTaskWoken` | `ptr` | used in ISR context |

**Returns** `u32`: bytes committed

**Notes:** Role inferred from the head update and the receiver-side notification. Counterpart of stream_buffer_consume_tail.

- Addresses by version: 219: 0x0C0438D8
- Called by: `ble_219_0c046468`
- Calls: `rtos_enter_critical`, `rtos_exit_critical`, `vTaskSuspendAll`, `xTaskResumeAll`, `xTaskGenericNotify`, `xTaskGenericNotifyFromISR`
- Confidence: medium

## stream_buffer_consume_tail

**Advance a stream buffer's tail by up to N stored bytes and wake a sender waiting for space**

Clamps the requested count to the bytes currently stored (head minus tail, modulo the length), moves xTail forward by that amount with wrap-around, and wakes the task waiting to send (xTaskWaitingToSend, +0x14). With the flag argument zero it runs in task context: scheduler suspended, xTaskGenericNotify, slot cleared, scheduler resumed. With a non-zero flag it runs in ISR context: rtos_enter_critical, xTaskGenericNotifyFromISR with pxHigherPriorityTaskWoken, rtos_exit_critical. Returns the number of bytes consumed. Internal helper of the stream buffer family.

| Parameter | Type | Description |
|---|---|---|
| `xStreamBuffer` | `ptr` | stream buffer |
| `uxBytes` | `u32` | bytes to consume |
| `fromISR` | `bool` | true for interrupt context |
| `pxHigherPriorityTaskWoken` | `ptr` | used in ISR context |

**Returns** `u32`: bytes consumed

**Notes:** Role inferred from the tail update and the sender-side notification. The name is descriptive, not the upstream one.

- Addresses by version: 219: 0x0C043830
- Calls: `rtos_enter_critical`, `rtos_exit_critical`, `vTaskSuspendAll`, `xTaskResumeAll`, `xTaskGenericNotify`, `xTaskGenericNotifyFromISR`
- Confidence: medium

## uxListRemove

**FreeRTOS: unlink an item from the list that contains it**

FreeRTOS uxListRemove: reads the owning list from pvContainer (+0x10), joins the item's neighbours, moves list->pxIndex to the previous item if it pointed at the removed one, clears pvContainer and decrements uxNumberOfItems. Returns the new item count of the list.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ListItem_t* to remove |

**Returns** `u32`: number of items left in the list

- Addresses by version: 219: 0x0C042A14
- Called by: `prvAddCurrentTaskToDelayedList`, `ble_219_0c043da0`, `xTaskIncrementTick`, `xTaskResumeAll`, `xTaskRemoveFromEventList`, `vTaskRemoveFromUnorderedEventList`, `xTaskPriorityInherit`, `xTaskPriorityDisinherit`, `vTaskPriorityDisinheritAfterTimeout`, `xTaskGenericNotify`, `xTaskGenericNotifyFromISR`, `prvInsertTimerInActiveList` ...
- Confidence: high

## uxQueueMessagesWaiting

**FreeRTOS: number of items currently in the queue, read inside a critical section**

taskENTER_CRITICAL (0x0c03f640), read uxMessagesWaiting (Queue_t +0x38), taskEXIT_CRITICAL (0x0c03f65c), return it. No direct callers in the image (reached through the CMSIS-RTOS2 wrapper table or inlined elsewhere). Sibling: uxQueueSpacesAvailable (0x0c043338).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | QueueHandle_t xQueue |

**Returns** `u32`: uxMessagesWaiting

- Addresses by version: 219: 0x0C043320
- Calls: `vPortEnterCritical`, `vPortExitCritical`
- Confidence: high

## uxQueueSpacesAvailable

**FreeRTOS: free slots in a queue (uxLength - uxMessagesWaiting) read inside a critical section**

taskENTER_CRITICAL (0x0c03f640), computes uxLength (+0x3C) - uxMessagesWaiting (+0x38), taskEXIT_CRITICAL (0x0c03f65c). Called from 0x0c0422d4 (CMSIS-RTOS2 osMessageQueueGetSpace-style wrapper). Sibling: uxQueueMessagesWaiting (0x0c043320).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | QueueHandle_t xQueue |

**Returns** `s32`: number of free item slots

- Addresses by version: 219: 0x0C043338
- Called by: `ble_ring_poll_status`
- Calls: `vPortEnterCritical`, `vPortExitCritical`
- Confidence: high

## uxTaskGetNumberOfTasks

**Return the RTOS word at DAT_2000cc14 (likely the number of tasks)**

Pure getter returning the kernel variable at 0x2000cc14. By its position among the FreeRTOS task globals (near the scheduler-suspended counter and scheduler-running flag) this is most likely uxCurrentNumberOfTasks, but it could be another task global such as the idle task handle. Only caller is ble_219_0c0360d4, which also calls xTaskGetCurrentTaskHandle.

**Returns** `u32`: value of DAT_2000cc14

**Notes:** Identity of the variable not verified.

- Addresses by version: 219: 0x0C043F28
- Called by: `ble_219_0c0360d4`
- Confidence: low

## uxTaskGetSystemState

**FreeRTOS uxTaskGetSystemState: snapshot TaskStatus_t entries for every task and the total run time**

Upstream uxTaskGetSystemState(pxTaskStatusArray, uxArraySize, pulTotalRunTime). It increments the scheduler suspension counter DAT_2000CC20 and, when the task count DAT_2000CC14 fits the array, fills it list by list through prvListTasksWithinSingleList (0x0C0444F4): the six ready lists from priority 5 down to 0, the delayed and overflow-delayed lists, the terminated list (state 4) and the suspended list (state 3). It writes the total run-time counter through the thunk at 0x0C073B70 when pulTotalRunTime is non-NULL, then resumes the scheduler and returns the entry count. It returns 0 when the array is too small.

| Parameter | Type | Description |
|---|---|---|
| `pxTaskStatusArray` | `ptr` | output array of TaskStatus_t |
| `uxArraySize` | `u32` | capacity of the array in entries |
| `pulTotalRunTime` | `ptr` | optional total run-time output |

**Returns** `u32`: entries written, or 0 when the array is too small

**Notes:** The six ready lists imply configMAX_PRIORITIES = 6, which agrees with the priority arithmetic in xQueueSemaphoreTake.

- Addresses by version: 219: 0x0C044544
- Called by: `ble_219_0c0360d4`
- Calls: `xTaskResumeAll`, `prvListTasksWithinSingleList`, `rtos_run_time_counter_get`
- Confidence: high

## uxTaskResetEventItemValue

**FreeRTOS: return and reset the current task's event list item value**

Reads the xEventListItem.xItemValue (TCB+0x18) of the current task, replaces it with 6 - uxPriority (TCB+0x2c; configMAX_PRIORITIES appears to be 6) and returns the old value. Used by notification/event-group wait code (caller ble_219_0c042858) to fetch the notification value that was stashed in the item.

**Returns** `u32`: previous event list item value

- Addresses by version: 219: 0x0C0447B8
- Called by: `xEventGroupWaitBits`
- Confidence: high

## vApplicationGetIdleTaskMemory

**Provide static TCB and stack buffers for the idle task (FreeRTOS static allocation)**

FreeRTOS configSUPPORT_STATIC_ALLOCATION callback: stores the address of the TCB buffer 0x2000cb2c in *param_1, the address of the stack buffer 0x2000c72c in *param_2 and the stack depth 0x100 words (1 KiB) in *param_3. The buffers are adjacent (0x2000c72c + 0x400 = 0x2000cb2c). Called from ble_219_0c043e70, which is most likely vTaskStartScheduler creating the idle task.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | out: StaticTask_t** receiving the TCB buffer pointer |
| `param_2` | `ptr` | out: StackType_t** receiving the stack buffer pointer |
| `param_3` | `ptr` | out: uint32_t* receiving the stack size in words (0x100) |

**Notes:** Could be the timer-task variant (vApplicationGetTimerTaskMemory) - idle assumed from the caller.

- Addresses by version: 219: 0x0C042800
- Called by: `ble_219_0c043e70`
- Confidence: medium

## vListInitialise

**FreeRTOS: initialise an empty list with its end marker**

FreeRTOS vListInitialise on a 0x14-byte List_t: sets pxIndex (offset 4) to the embedded xListEnd mini item at offset 8, sets xListEnd.xItemValue to 0xFFFFFFFF (portMAX_DELAY) so it always sorts last, points xListEnd.pxNext (+0xc) and pxPrevious (+0x10) back at itself and sets uxNumberOfItems (offset 0) to 0. Used by the kernel task lists and queues.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | List_t* to initialise |

- Addresses by version: 219: 0x0C0429A4
- Called by: `xEventGroupCreateStatic`, `ble_219_0c04283c`, `xQueueGenericReset`, `prvInitialiseNewQueue`, `ble_219_0c042c08`, `prvInitialiseMutex`, `ble_219_0c042e44`, `prvAddNewTaskToReadyList`, `prvCheckForValidListAndQueue`
- Confidence: high

## vListInitialiseItem

**FreeRTOS: mark a list item as not belonging to any list**

FreeRTOS vListInitialiseItem: stores 0 in pvContainer (offset 0x10) of the ListItem_t so listIS_CONTAINED_WITHIN reports false.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ListItem_t* to initialise |

- Addresses by version: 219: 0x0C0429BC
- Called by: `prvInitialiseNewTask`, `ble_219_0c044c7c`
- Confidence: high

## vListInsert

**FreeRTOS: insert an item into a list sorted by xItemValue**

FreeRTOS vListInsert: if the new item's xItemValue is 0xFFFFFFFF (portMAX_DELAY) it is inserted just before the list end marker; otherwise the list is walked from the end marker (list+8) until the following item has a value greater than the new item's value (stable, ascending). The item is spliced in, pvContainer (+0x10) set to the list and uxNumberOfItems incremented. Used for delayed-task lists and priority-ordered event lists.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | List_t* destination list |
| `param_2` | `ptr` | ListItem_t* item to insert; item->xItemValue is the sort key |

- Addresses by version: 219: 0x0C0429E4
- Called by: `prvAddCurrentTaskToDelayedList`, `vTaskPlaceOnEventList`, `prvInsertTimerInActiveList`, `ble_219_0c044c7c`, `prvSwitchTimerLists`, `ble_219_0c044ee8`
- Confidence: high

## vListInsertEnd

**FreeRTOS: insert an item at the end of a list (before pxIndex)**

FreeRTOS vListInsertEnd: links param_2 immediately before the list's pxIndex item (list+4), i.e. at the logical end of the round-robin ring: new->pxNext (+4) = pxIndex, new->pxPrevious (+8) = pxIndex->pxPrevious, the neighbours are re-linked, new->pvContainer (+0x10) = list and uxNumberOfItems (list+0) is incremented. Used for ready lists and event lists.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | List_t* destination list |
| `param_2` | `ptr` | ListItem_t* item to insert |

- Addresses by version: 219: 0x0C0429C4
- Called by: `prvAddNewTaskToReadyList`, `prvAddCurrentTaskToDelayedList`, `ble_219_0c043da0`, `xTaskIncrementTick`, `xTaskResumeAll`, `vTaskPlaceOnUnorderedEventList`, `vTaskPlaceOnEventListRestricted`, `xTaskRemoveFromEventList`, `vTaskRemoveFromUnorderedEventList`, `xTaskPriorityInherit`, `xTaskPriorityDisinherit`, `vTaskPriorityDisinheritAfterTimeout` ...
- Confidence: high

## vPortEnterCritical

**FreeRTOS port: raise BASEPRI, increment uxCriticalNesting (DAT_20003ec4), DSB+ISB**

Calls rtos_enter_critical (BASEPRI = 0x40, masking all interrupts of lower priority), increments the critical-nesting counter DAT_20003ec4 and executes DSB/ISB. Dozens of callers across the FreeRTOS task/queue/timer code (0x0c03feac, 0x0c0400cc, 0x0c0422d4 ...). Paired with vPortExitCritical; the counter is reset to 0 by xPortStartScheduler.

**Notes:** The saved BASEPRI returned by rtos_enter_critical is discarded; unlike stock FreeRTOS the interrupt mask value is 0x40.

- Addresses by version: 219: 0x0C03F640
- Called by: `clock_gettime`, `gettimeofday`, `ble_ring_poll_status`, `ble_219_0c0424d8`, `ble_219_0c04264c`, `xEventGroupWaitBits`, `xEventGroupClearBits`, `prvUnlockQueue`, `xQueueGenericReset`, `prvInitialiseNewQueue`, `ble_219_0c042c08`, `xQueueGenericSend` ...
- Calls: `rtos_enter_critical`
- Confidence: high

## vPortExitCritical

**FreeRTOS port: decrement uxCriticalNesting (DAT_20003ec4) and re-enable interrupts when it reaches 0**

Decrements the critical-nesting counter DAT_20003ec4; if it becomes 0 calls rtos_exit_critical to lower BASEPRI (interrupts enabled again), otherwise returns with interrupts still masked. Counterpart of vPortEnterCritical, same callers.

**Notes:** The argument passed to rtos_exit_critical is not visible in the decompile (presumably 0).

- Addresses by version: 219: 0x0C03F65C
- Called by: `clock_gettime`, `gettimeofday`, `ble_ring_poll_status`, `ble_219_0c0424d8`, `ble_219_0c04264c`, `xEventGroupWaitBits`, `xEventGroupClearBits`, `prvUnlockQueue`, `xQueueGenericReset`, `prvInitialiseNewQueue`, `ble_219_0c042c08`, `xQueueGenericSend` ...
- Calls: `rtos_exit_critical`
- Confidence: high

## vPortSetupTimerInterrupt

**FreeRTOS port: program SysTick for a 1 ms tick (LOAD = clk/1000 - 1, CTRL = ENABLE|TICKINT)**

Writes SysTick CTRL (0xE000E010) = 0 and VAL (0xE000E018) = 0, obtains the SysTick reference clock frequency in Hz from the RAM-resident routine ble_ram_patch_thunk_20000554, sets LOAD (0xE000E014) = freq / 1000 - 1 and finally CTRL = 3 (ENABLE | TICKINT, CLKSOURCE = 0 i.e. external reference clock). Called from the scheduler start routine 0x0c043e70 (xPortStartScheduler: sets PendSV/SysTick priorities in SHPR3, computes BogoMIPS, zeroes uxCriticalNesting) just before the first task is started.

- Addresses by version: 219: 0x0C03F600
- Peripheral registers: `0xe000e010` (W), `0xe000e014` (W), `0xe000e018` (W)
- Called by: `ble_219_0c043e70`
- Calls: `ble_ram_patch_thunk_20000554`
- Confidence: high

## vQueueWaitForMessageRestricted

**FreeRTOS vQueueWaitForMessageRestricted: block the caller on an empty queue without a wake-up time**

Upstream vQueueWaitForMessageRestricted(xQueue, xTicksToWait, xWaitIndefinitely). Inside a critical section it changes the RX and TX lock counts from unlocked (-1) to zero. If the queue is still empty it places the caller on xTasksWaitingToReceive with vTaskPlaceOnEventListRestricted, which uses no wake-up time when xWaitIndefinitely is set. It then unlocks the queue with prvUnlockQueue. Called from ble_219_0c044ee8.

| Parameter | Type | Description |
|---|---|---|
| `xQueue` | `ptr` | queue handle |
| `xTicksToWait` | `u32` | timeout in ticks |
| `xWaitIndefinitely` | `bool` | block without a timeout |

- Addresses by version: 219: 0x0C043380
- Called by: `ble_219_0c044ee8`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `prvUnlockQueue`, `vTaskPlaceOnEventListRestricted`
- Confidence: high

## vTaskDelay

**FreeRTOS vTaskDelay: block the calling task for a number of ticks, with zero only yielding**

With zero ticks it only requests a context switch through rtos_pendsv_trigger. Otherwise it increments the scheduler suspension counter DAT_2000CC20 (uxSchedulerSuspended), moves the running task to the delayed list with prvAddCurrentTaskToDelayedList (0x0C043A7C), calls xTaskResumeAll (0x0C0440AC) and yields only if that call did not already yield.

| Parameter | Type | Description |
|---|---|---|
| `xTicksToDelay` | `u32` | delay in ticks |

- Addresses by version: 219: 0x0C0441A8
- Called by: `ble_219_0c0287ac`, `ble_219_0c028c94`, `ble_219_0c029230`, `ble_219_0c02c49c`, `ble_219_0c04542c`, `ble_219_0c046e04`, `ble_fd_select`, `ble_219_0c0593a4`, `ble_219_0c0598b8`, `ble_219_0c05a608`
- Calls: `rtos_pendsv_trigger`, `prvAddCurrentTaskToDelayedList`, `xTaskResumeAll`
- Confidence: high

## vTaskGetInfo

**FreeRTOS vTaskGetInfo: fill a TaskStatus_t for a task, deriving its state and stack high-water mark**

Upstream vTaskGetInfo(xTask, pxTaskStatus, xGetFreeStackSpace, eState). A NULL handle means the current task. It fills the 9-word TaskStatus_t (36 bytes) with the handle, the name pointer (TCB +0x34), the task number (+0x44), the priority (+0x2C), the stack base and a run-time counter field. When eState is 5 (eInvalid) it derives the state from the list the task sits in: the current TCB gives 0 (eRunning); the delayed lists give 2 (eBlocked); the suspended list gives 3 (eSuspended), or 2 when the task is blocked on an event; the terminated-tasks list or no list gives 4 (eDeleted); any other list gives 1 (eReady). With xGetFreeStackSpace set it counts leading 0xA5 fill bytes from the stack base and reports the count in words (bytes divided by 4).

| Parameter | Type | Description |
|---|---|---|
| `xTask` | `ptr` | task handle, NULL for the current task |
| `pxTaskStatus` | `ptr` | output TaskStatus_t, 36 bytes |
| `xGetFreeStackSpace` | `bool` | compute the stack high-water mark |
| `eState` | `s32` | task state, or 5 to derive it from the list |

**Notes:** Field offsets of the run-time counter and the high-water mark are only partly visible in the decompile, so the exact field names inside TaskStatus_t are not asserted.

- Addresses by version: 219: 0x0C044400
- Called by: `ble_219_0c035fc0`, `prvListTasksWithinSingleList`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `xTaskResumeAll`
- Confidence: high

## vTaskInternalSetTimeOutState

**FreeRTOS: record overflow count and tick count in a TimeOut_t**

Fills param_1: [0] = xNumOfOverflows (DAT_2000cc5c), [1] = xTickCount (DAT_2000cca0). Used by queue send/receive (xQueueGenericSend/Receive/SemaphoreTake) to start a blocking-timeout measurement.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TimeOut_t* output {xOverflowCount, xTimeOnEntering} |

- Addresses by version: 219: 0x0C044360
- Called by: `xQueueGenericSend`, `xQueueReceive`, `xQueueSemaphoreTake`, `xQueuePeek`
- Confidence: high

## vTaskMissedYield

**FreeRTOS: flag that a context switch was requested while the scheduler was suspended**

Sets xYieldPending (DAT_2000cca4) to 1; xTaskResumeAll yields when it later finds this flag set. Called from ble_219_0c042aac.

- Addresses by version: 219: 0x0C0443F4
- Called by: `prvUnlockQueue`
- Confidence: high

## vTaskPlaceOnEventList

**FreeRTOS: block the current task on a sorted event list with a timeout**

tasks.c vTaskPlaceOnEventList(pxEventList, xTicksToWait). Inserts pxCurrentTCB->xEventListItem (DAT_2000cb8c + 0x18) into the given event list with the priority-sorted vListInsert (item value = 6 - priority, so highest priority wakes first), then calls prvAddCurrentTaskToDelayedList(xTicksToWait, pdTRUE). Must be called with the scheduler suspended; used by the queue send/receive/semaphore-take paths (0x0c042c8c, 0x0c042fa4, 0x0c0430a8, 0x0c043224) to block on xTasksWaitingToSend/Receive.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | List_t* event list to wait on |
| `param_2` | `u32` | xTicksToWait (ticks) |

- Addresses by version: 219: 0x0C0441F0
- Called by: `xQueueGenericSend`, `xQueueReceive`, `xQueueSemaphoreTake`, `xQueuePeek`
- Calls: `vListInsert`, `prvAddCurrentTaskToDelayedList`
- Confidence: high

## vTaskPlaceOnEventListRestricted

**FreeRTOS: block the current task on an event list, optionally forever (timer task)**

tasks.c vTaskPlaceOnEventListRestricted(pxEventList, xTicksToWait, xWaitIndefinitely). Appends pxCurrentTCB->xEventListItem (DAT_2000cb8c + 0x18) to the list with vListInsertEnd; if xWaitIndefinitely is set the wait is forced to portMAX_DELAY, then prvAddCurrentTaskToDelayedList(xTicksToWait, xWaitIndefinitely) is called. Used only by the timer-service path (prvProcessTimerOrBlockTask, 0x0c043380, blocking on the timer command queue at +0x24 of the queue struct).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | List_t* event list |
| `param_2` | `u32` | xTicksToWait (ticks) |
| `param_3` | `bool` | xWaitIndefinitely |

- Addresses by version: 219: 0x0C044238
- Called by: `vQueueWaitForMessageRestricted`
- Calls: `vListInsertEnd`, `prvAddCurrentTaskToDelayedList`
- Confidence: high

## vTaskPlaceOnUnorderedEventList

**FreeRTOS: block the current task on an unordered event list (event groups)**

tasks.c vTaskPlaceOnUnorderedEventList(pxEventList, xItemValue, xTicksToWait). Stores xItemValue | taskEVENT_LIST_ITEM_VALUE_IN_USE (0x80000000) in pxCurrentTCB->xEventListItem.xItemValue (DAT_2000cb8c + 0x18), appends the item to the list with vListInsertEnd (FIFO, not priority ordered) and calls prvAddCurrentTaskToDelayedList(xTicksToWait, pdTRUE). The item value carries the event-group wait bits/flags and is read back by uxTaskResetEventItemValue. Single caller: the event-group wait routine 0x0c042858.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | List_t* event list |
| `param_2` | `u32` | xItemValue (bits to wait for plus control flags) |
| `param_3` | `u32` | xTicksToWait (ticks) |

- Addresses by version: 219: 0x0C044210
- Called by: `xEventGroupWaitBits`
- Calls: `vListInsertEnd`, `prvAddCurrentTaskToDelayedList`
- Confidence: high

## vTaskPriorityDisinheritAfterTimeout

**FreeRTOS: lower a mutex holder's priority after a waiter timed out**

tasks.c vTaskPriorityDisinheritAfterTimeout(pxMutexHolder, uxHighestPriorityWaitingTask). Ignores NULL. uxPriorityToUse = max(uxBasePriority +0x4c, highest waiting priority). Only acts when uxPriority (+0x2c) differs and the holder holds exactly one mutex (uxMutexesHeld +0x50 == 1): writes the new priority, updates xEventListItem.xItemValue (+0x18) to 6 - priority unless bit 31 (in-use) is set, and if the task is in its ready list (container +0x14 == &pxReadyTasksLists[old]) moves it to pxReadyTasksLists[new] (0x2000cb98 + prio*20) adjusting uxTopReadyPriority (DAT_2000cc28). Called from the semaphore take path 0x0c0430a8 when a mutex wait times out.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TCB_t* mutex holder (may be NULL) |
| `param_2` | `u32` | highest priority among tasks still waiting for the mutex |

- Addresses by version: 219: 0x0C044744
- Called by: `xQueueSemaphoreTake`
- Calls: `vListInsertEnd`, `uxListRemove`
- Confidence: high

## vTaskRemoveFromUnorderedEventList

**FreeRTOS: wake a task from an unordered event list and hand it the result value**

tasks.c vTaskRemoveFromUnorderedEventList(pxEventListItem, xItemValue). Writes xItemValue | 0x80000000 (taskEVENT_LIST_ITEM_VALUE_IN_USE) into the list item, fetches its owner TCB (+0xc), removes the event item and the task's xStateListItem (+4), raises uxTopReadyPriority (DAT_2000cc28) and appends the task to pxReadyTasksLists[uxPriority] (0x2000cb98 + prio*20). If the woken task outranks pxCurrentTCB (DAT_2000cb8c + 0x2c) xYieldPending (DAT_2000cca4) is set so the caller yields after resuming the scheduler. Must be called with the scheduler suspended. Single caller: the event-group set-bits routine 0x0c04291c. The extra decompiled arguments param_3/param_4 are artefacts.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | ListItem_t* xEventListItem of the task to wake |
| `param_2` | `u32` | xItemValue to deliver (event bits) |

- Addresses by version: 219: 0x0C0442E4
- Called by: `xEventGroupSetBits`
- Calls: `vListInsertEnd`, `uxListRemove`
- Confidence: high

## vTaskSetTimeOutState

**FreeRTOS: record overflow count and tick count in a TimeOut_t inside a critical section**

tasks.c vTaskSetTimeOutState(pxTimeOut): the public, critical-section-protected version of vTaskInternalSetTimeOutState (0x0c044360). Between vPortEnterCritical/vPortExitCritical (0x0c03f640/0x0c03f65c) it stores xNumOfOverflows (DAT_2000cc5c) in [0] (xOverflowCount) and xTickCount (DAT_2000cca0) in [1] (xTimeOnEntering). Used by the stream-buffer receive path (0x0c043554) before blocking with xTaskNotifyWait.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TimeOut_t* output {xOverflowCount, xTimeOnEntering} |

- Addresses by version: 219: 0x0C04433C
- Called by: `xStreamBufferSend`
- Calls: `vPortEnterCritical`, `vPortExitCritical`
- Confidence: high

## vTaskSuspendAll

**FreeRTOS: suspend the scheduler by incrementing the nesting counter**

Increments uxSchedulerSuspended (DAT_2000cc20). Nesting is allowed; xTaskResumeAll decrements it. Called at the start of queue, timer and event-group operations (12 callers).

- Addresses by version: 219: 0x0C043F0C
- Called by: `xEventGroupWaitBits`, `xEventGroupSetBits`, `xQueueGenericSend`, `xQueueReceive`, `xQueueSemaphoreTake`, `xQueuePeek`, `xStreamBufferSend`, `xStreamBufferReceive`, `stream_buffer_consume_tail`, `stream_buffer_commit_head`, `ble_219_0c044ee8`, `ble_219_0c046e04`
- Confidence: high

## xEventGroupClearBits

**FreeRTOS: clear bits in an event group inside a critical section and return the previous value**

taskENTER_CRITICAL (0x0c03f640), uxReturn = pxEventBits->uxEventBits (word at +0), uxEventBits &= ~uxBitsToClear, taskEXIT_CRITICAL (0x0c03f65c), return uxReturn. Exactly FreeRTOS event_groups.c xEventGroupClearBits without the trace macros. Called from 0x0c048298 (CMSIS-RTOS2 osEventFlagsClear-style wrapper).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | EventGroupHandle_t (uxEventBits at offset 0) |
| `param_2` | `u32` | uxBitsToClear |

**Returns** `u32`: event bits before clearing

- Addresses by version: 219: 0x0C042900
- Called by: `ble_evt_clear_index_bit`
- Calls: `vPortEnterCritical`, `vPortExitCritical`
- Confidence: high

## xEventGroupCreateStatic

**FreeRTOS: initialise a caller-provided StaticEventGroup_t and return it as the event group handle**

If the buffer is non-NULL: uxEventBits (+0) = 0, vListInitialise(&xTasksWaitingForBits) at +4 (20-byte List_t), and ucStaticallyAllocated at +0x1C = pdTRUE (the offset implies configUSE_TRACE_FACILITY = 1, with uxEventGroupNumber at +0x18). Returns the same pointer (NULL in, NULL out). Called from 0x0c047f70 and 0x0c048260 (CMSIS-RTOS2 / LibWhale wrappers). Companion: xEventGroupClearBits at 0x0c042900.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | StaticEventGroup_t storage (32 bytes) |

**Returns** `ptr`: EventGroupHandle_t = param_1, or NULL

- Addresses by version: 219: 0x0C04281C
- Called by: `posix_event_2000f65c_init`, `posix_select_event_init`
- Calls: `vListInitialise`
- Confidence: high

## xEventGroupSetBits

**FreeRTOS xEventGroupSetBits: OR bits into the group and wake matching waiters**

Under vTaskSuspendAll it ORs the new bits into the stored word, then walks the waiting list at +4 (xTasksWaitingForBits). A waiter is woken when its condition holds with its mask (low 28 bits of the list value): any bit for wait-any, all bits for wait-all (flag 0x40000000). Woken waiters go through 0x0C0442E4 with the bits or 0x20000000 so they know they were released by a bit set. Waiters that asked for clear-on-exit (flag 0x10000000) contribute their mask to a set that is cleared from the group before returning. The function ends with xTaskResumeAll and returns the stored bits after that clear. Part of the event group family with xEventGroupWaitBits.

| Parameter | Type | Description |
|---|---|---|
| `pxEventBits` | `ptr` | event group |
| `uxBitsToSet` | `u32` | bits to set |

**Returns** `u32`: stored event bits after the clear-on-exit bits were removed

**Notes:** Flag layout as in xEventGroupWaitBits.

- Addresses by version: 219: 0x0C04291C
- Called by: `ble_evt_set_index_bit`, `ble_signal_worker_event`, `ble_deferred_list_post`, `ble_219_0c05d260`, `ble_xfer_pump_chunk_and_notify`, `ble_sched_signal_event`
- Calls: `vTaskSuspendAll`, `xTaskResumeAll`, `vTaskRemoveFromUnorderedEventList`
- Confidence: high

## xEventGroupWaitBits

**FreeRTOS xEventGroupWaitBits: wait for event bits, blocking on the group's unordered list**

Upstream FreeRTOS xEventGroupWaitBits(pxEventBits, uxBitsToWaitFor, xClearOnExit, xWaitForAllBits, xTicksToWait) in this port's layout. Flags sit in the top bits of the stored word: 0x10000000 = clear on exit, 0x40000000 = wait for all bits, 0x20000000 = set by the wake side when unblocked by bits. The event bits are the low 28 bits. Under vTaskSuspendAll it tests the bits; if the condition is met it returns them, clearing them first when clear-on-exit was requested. Otherwise, with a non-zero timeout, it places the task on the group's unordered list (0x0C044210), resumes the scheduler (yielding through rtos_pendsv_trigger when needed), and on wake-up returns at once if the unblock came from a bit set, or re-reads the bits, clears them when satisfied and returns on timeout. Part of the event group family with xEventGroupSetBits.

| Parameter | Type | Description |
|---|---|---|
| `pxEventBits` | `ptr` | event group |
| `uxBitsToWaitFor` | `u32` | bit mask to wait for |
| `xClearOnExit` | `bool` | clear the waited bits when the wait completes |
| `xWaitForAllBits` | `bool` | true to require every bit in the mask |
| `xTicksToWait` | `u32` | timeout in ticks; 0 means no blocking |

**Returns** `u32`: event bits at the time the wait completed

**Notes:** The flag constants 0x10000000, 0x20000000 and 0x40000000 differ from upstream FreeRTOS (0x01000000 and so on), so this build uses its own layout.

- Addresses by version: 219: 0x0C042858
- Called by: `ble_fd_select`, `ble_219_0c0599d4`, `ble_219_0c05d108`
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `vTaskSuspendAll`, `xTaskResumeAll`, `vTaskPlaceOnUnorderedEventList`, `uxTaskResetEventItemValue`
- Confidence: high

## xQueueGenericReset

**FreeRTOS queue.c: reset a queue to empty and (optionally) re-initialise its wait lists**

Inside taskENTER/EXIT_CRITICAL (0x0c03f640/0x0c03f65c): uxMessagesWaiting (+0x38) = 0, cRxLock (+0x44) and cTxLock (+0x45) = queueUNLOCKED (0xFF), pcTail (+4) = pcHead + uxLength*uxItemSize (+0x3C * +0x40), pcWriteTo (+8) = pcHead, pcReadFrom (+0xC) = pcTail - uxItemSize. If xNewQueue == pdFALSE and a task is blocked in xTasksWaitingToSend (+0x10), xTaskRemoveFromEventList (0x0c044264) unblocks it and, if it has higher priority, rtos_pendsv_trigger() (queueYIELD_IF_USING_PREEMPTION) requests a context switch; if xNewQueue is true both wait lists (+0x10 and +0x24) are initialised with vListInitialise. Always returns pdPASS (1). No direct callers in the image (the create path at 0x0c042ba0 inlines the same code).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | Queue_t *xQueue |
| `param_2` | `s32` | xNewQueue: non-zero for a freshly created queue |

**Returns** `u32`: pdPASS (1)

- Addresses by version: 219: 0x0C042B38
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `vListInitialise`, `xTaskRemoveFromEventList`
- Confidence: high

## xQueueGenericSend

**FreeRTOS xQueueGenericSend: copy an item into a queue, blocking up to a tick timeout when full**

Upstream queue.c xQueueGenericSend(xQueue, pvItemToQueue, xTicksToWait, xCopyPosition); copy positions are 0 back, 1 front and 2 overwrite. It loops inside a critical section. When there is space, or the overwrite position is used, it copies with prvCopyDataToQueue, wakes a waiting receiver through xTaskRemoveFromEventList (yielding if that task outranks the caller) and returns 1. When the queue is full it returns 0 at zero timeout. Otherwise it records a timeout state (vTaskInternalSetTimeOutState), places the caller on xTasksWaitingToSend with vTaskPlaceOnEventList, unlocks the queue with prvUnlockQueue and retries via xTaskCheckForTimeOut. Scheduler suspension brackets the wait logic. Part of the FreeRTOS queue family in this packet.

| Parameter | Type | Description |
|---|---|---|
| `xQueue` | `ptr` | queue handle |
| `pvItemToQueue` | `ptr` | item to copy in; NULL for mutex or semaphore give |
| `xTicksToWait` | `u32` | timeout in ticks |
| `xCopyPosition` | `u32` | 0 back, 1 front, 2 overwrite |

**Returns** `s32`: 1 when the item was queued or the token given, 0 on timeout

- Addresses by version: 219: 0x0C042C8C
- Called by: `ble_219_0c028b90`, `ble_219_0c029284`, `ble_219_0c02b480`, `ble_219_0c02e5a4`, `ble_219_0c02e758`, `ble_219_0c0354cc`, `ble_219_0c0424d8`, `prvInitialiseMutex`, `xQueueGiveMutexRecursive`, `rtos_mutex_give_checked`, `ble_219_0c042e44`, `xTimerGenericCommand` ...
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `prvCopyDataToQueue`, `prvUnlockQueue`, `vTaskSuspendAll`, `xTaskResumeAll`, `vTaskPlaceOnEventList`, `xTaskRemoveFromEventList`, `vTaskInternalSetTimeOutState`, `xTaskCheckForTimeOut`
- Confidence: high

## xQueueGenericSendFromISR

**FreeRTOS xQueueGenericSendFromISR: queue an item from interrupt context inside a critical section**

Enters the port critical section with rtos_enter_critical, which returns the previous BASEPRI. If there is space, or the overwrite position is used, it saves the TX lock count, copies the item with prvCopyDataToQueue and then either increments the TX lock count (queue locked, wake-up deferred to prvUnlockQueue) and returns 1, or wakes a waiting receiver through xTaskRemoveFromEventList and sets *pxHigherPriorityTaskWoken to 1 when the woken task has higher priority. Returns 0 when the queue is full. BASEPRI is restored with rtos_exit_critical on exit. Part of the FreeRTOS queue family in this packet.

| Parameter | Type | Description |
|---|---|---|
| `xQueue` | `ptr` | queue handle |
| `pvItemToQueue` | `ptr` | item to copy in |
| `pxHigherPriorityTaskWoken` | `ptr` | receives 1 on a higher-priority wake-up; may be NULL |
| `xCopyPosition` | `u32` | 0 back, 1 front, 2 overwrite |

**Returns** `s32`: 1 when the item was queued, 0 when the queue was full

- Addresses by version: 219: 0x0C042EB4
- Called by: `rtos_timer_pend_fixed_callback_from_isr`, `xTimerGenericCommand`, `ble_219_0c0467b8`
- Calls: `rtos_enter_critical`, `rtos_exit_critical`, `prvCopyDataToQueue`, `xTaskRemoveFromEventList`
- Confidence: high

## xQueueGiveFromISR

**FreeRTOS queue.c: give a semaphore from an ISR, waking a waiting receiver if the queue is unlocked**

Masks interrupts with rtos_enter_critical() (portSET_INTERRUPT_MASK_FROM_ISR). If uxMessagesWaiting (+0x38) < uxLength (+0x3C): increments the count; if cTxLock (+0x45) is not queueUNLOCKED (-1) it just increments the lock counter (a later prvUnlockQueue will wake receivers); otherwise, if xTasksWaitingToReceive (+0x24) is non-empty and xTaskRemoveFromEventList (0x0c044264) reports a higher-priority task and pxHigherPriorityTaskWoken is non-NULL, *pxHigherPriorityTaskWoken = pdTRUE. Returns pdPASS (1). If the queue is full returns errQUEUE_FULL (0). Interrupt mask restored with rtos_exit_critical in every path. No data copy (semaphore only). Called from 0x0c04533c (HCI/ISR glue).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | QueueHandle_t (semaphore) xQueue |
| `param_2` | `ptr` | BaseType_t *pxHigherPriorityTaskWoken, may be NULL |

**Returns** `u32`: pdPASS (1) or errQUEUE_FULL (0)

- Addresses by version: 219: 0x0C042F38
- Called by: `ble_219_0c04533c`
- Calls: `rtos_enter_critical`, `rtos_exit_critical`, `xTaskRemoveFromEventList`
- Confidence: high

## xQueueGiveMutexRecursive

**FreeRTOS xQueueGiveMutexRecursive: release one level of a recursive mutex the caller holds**

Checks that the caller (xTaskGetCurrentTaskHandle) is the mutex holder stored at +4; if not it returns 0 and changes nothing. Otherwise it decrements the recursion count at +0xC. When the count reaches zero it releases the mutex with ble_219_0c042c8c (xQueueGenericSend with a NULL item and zero timeout). Returns 1 in both the nested and the final release case.

| Parameter | Type | Description |
|---|---|---|
| `xMutex` | `ptr` | recursive mutex handle |

**Returns** `s32`: 1 when the caller held the mutex and released one level, 0 otherwise

- Addresses by version: 219: 0x0C042DF4
- Called by: `ble_219_0c02dc50`, `ble_219_0c02dea8`, `ble_219_0c035900`, `ble_stack_lock_give`, `ble_pktq_enqueue`, `ble_219_0c05d260`, `ble_219_0c05d2c0`, `ble_xfer_pump_chunk_and_notify`, `ble_219_0c05d358`
- Calls: `xQueueGenericSend`, `xTaskGetCurrentTaskHandle`
- Confidence: high

## xQueuePeek

**FreeRTOS xQueuePeek: copy the head item to a buffer without removing it, with optional blocking**

Upstream xQueueGenericReceive with xJustPeek true. Like xQueueReceive it waits for an item when the queue is empty. When an item is present it copies the head item with memcpy (0x0C0709BC) but restores the read pointer afterwards, so the item stays queued. It wakes another task waiting on xTasksWaitingToReceive, as upstream does, and otherwise uses the same critical section, timeout and blocking code as xQueueReceive. Part of the FreeRTOS queue family in this packet.

| Parameter | Type | Description |
|---|---|---|
| `xQueue` | `ptr` | queue handle |
| `pvBuffer` | `ptr` | destination buffer for one item |
| `xTicksToWait` | `u32` | timeout in ticks |

**Returns** `s32`: 1 when an item was peeked, 0 on timeout

- Addresses by version: 219: 0x0C043224
- Called by: `ble_219_0c02dc50`
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `prvUnlockQueue`, `vTaskSuspendAll`, `xTaskResumeAll`, `vTaskPlaceOnEventList`, `xTaskRemoveFromEventList`, `vTaskInternalSetTimeOutState`, `xTaskCheckForTimeOut`, `memcpy`
- Confidence: high

## xQueueReceive

**FreeRTOS xQueueReceive: dequeue one item into a buffer, blocking up to a tick timeout when empty**

Upstream xQueueGenericReceive with xJustPeek false. Inside a critical section, when uxMessagesWaiting is non-zero it advances the read pointer by one item (wrapping at the end of the buffer), copies the item out with memcpy (0x0C0709BC), decrements uxMessagesWaiting and wakes one task blocked on xTasksWaitingToSend through xTaskRemoveFromEventList. It returns 1. When the queue is empty and the timeout is zero it returns 0. Otherwise it records the timeout state, blocks on xTasksWaitingToReceive with vTaskPlaceOnEventList, unlocks the queue (prvUnlockQueue) and retries. Part of the FreeRTOS queue family in this packet.

| Parameter | Type | Description |
|---|---|---|
| `xQueue` | `ptr` | queue handle |
| `pvBuffer` | `ptr` | destination buffer for one item |
| `xTicksToWait` | `u32` | timeout in ticks |

**Returns** `s32`: 1 when an item was received, 0 on timeout

- Addresses by version: 219: 0x0C042FA4
- Called by: `ble_219_0c02dc50`, `ble_219_0c04264c`, `ble_219_0c044ee8`, `ble_219_0c05d108`
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `prvUnlockQueue`, `vTaskSuspendAll`, `xTaskResumeAll`, `vTaskPlaceOnEventList`, `xTaskRemoveFromEventList`, `vTaskInternalSetTimeOutState`, `xTaskCheckForTimeOut`, `memcpy`
- Confidence: high

## xQueueSemaphoreTake

**FreeRTOS xQueueSemaphoreTake: take a semaphore or mutex token, with priority inheritance for mutexes**

Upstream xQueueSemaphoreGenericTake. If a token is available (uxMessagesWaiting non-zero) it decrements the count. For a mutex (pcHead NULL) it records the holder as pvTaskIncrementMutexHeldCount() in +4 and wakes a waiting giver through xTaskRemoveFromEventList. With a non-zero timeout and no token it records the timeout state and, for a mutex, raises the holder's priority with xTaskPriorityInherit (0x0C044658). It then blocks on xTasksWaitingToReceive and on timeout undoes the inheritance with vTaskPriorityDisinheritAfterTimeout (0x0C044744), using the highest waiter priority derived from the wait list head (6 minus its value). Part of the FreeRTOS queue family in this packet.

| Parameter | Type | Description |
|---|---|---|
| `xSemaphore` | `ptr` | semaphore or mutex handle |
| `xTicksToWait` | `s32` | timeout in ticks; -1 waits forever |

**Returns** `s32`: 1 when the token was taken, 0 on timeout

**Notes:** The 6 in the priority expression matches the configMAX_PRIORITIES value used by the task list code (six ready lists).

- Addresses by version: 219: 0x0C0430A8
- Called by: `ble_219_0c028b90`, `ble_219_0c029284`, `ble_219_0c02b480`, `ble_219_0c02e5a4`, `ble_219_0c02e758`, `xQueueTakeMutexRecursive`, `hal_i2c_dev_write`, `ble_i2c_write_read_locked`, `ble_219_0c048138`, `ble_219_0c048204`, `ble_219_0c0482e4`, `ble_fd_find_next_open` ...
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `prvUnlockQueue`, `vTaskSuspendAll`, `xTaskResumeAll`, `vTaskPlaceOnEventList`, `xTaskRemoveFromEventList`, `vTaskInternalSetTimeOutState`, `xTaskCheckForTimeOut`, `xTaskPriorityInherit`, `vTaskPriorityDisinheritAfterTimeout`, `pvTaskIncrementMutexHeldCount`
- Confidence: high

## xQueueTakeMutexRecursive

**FreeRTOS xQueueTakeMutexRecursive: take a recursive mutex, re-entering when the caller already holds it**

If the caller (xTaskGetCurrentTaskHandle) already holds the mutex at +4, only the recursion count at +0xC is incremented. Otherwise it calls xQueueSemaphoreTake (0x0C0430A8) with the given timeout and, on success, increments the recursion count. Part of the FreeRTOS queue family in this packet.

| Parameter | Type | Description |
|---|---|---|
| `xMutex` | `ptr` | recursive mutex handle |
| `xTicksToWait` | `s32` | timeout in ticks |

**Notes:** The decompiled function returns nothing, so the upstream pdPASS / pdFAIL result is not visible in this packet.

- Addresses by version: 219: 0x0C0431F8
- Called by: `ble_219_0c02dc50`, `ble_219_0c02dea8`, `ble_219_0c035900`, `ble_stack_lock_take`, `ble_219_0c048380`, `ble_pktq_enqueue`, `ble_219_0c05d260`, `ble_219_0c05d2c0`, `ble_xfer_pump_chunk_and_notify`, `ble_219_0c05d358`
- Calls: `xQueueSemaphoreTake`, `xTaskGetCurrentTaskHandle`
- Confidence: high

## xStreamBufferGenericCreateStatic

**FreeRTOS: initialise a static stream/message buffer (size, trigger level, storage, flags)**

Returns NULL if the storage area (param_4) is NULL. Otherwise, when the StaticStreamBuffer_t (param_5) is non-NULL, it does the work of prvInitialiseNewStreamBuffer: memset(pxStreamBuffer, 0, 0x24), xLength (+8) = xBufferSizeBytes, xTriggerLevelBytes (+0xC) = max(1, xTriggerLevelBytes), pucBuffer (+0x18) = storage and ucFlags (+0x1C) = sbFLAGS_IS_STATIC (2) | (xIsMessageBuffer ? sbFLAGS_IS_MESSAGE_BUFFER (1) : 0), i.e. 3 for a message buffer and 2 for a stream buffer. Returns param_5 (NULL if it was NULL). Callers: the UART dispatcher start routine 0x0c02e420, 0x0c0355c8 and the HCI intersys open 0x0c04542c, all supplying static storage.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | xBufferSizeBytes |
| `param_2` | `u32` | xTriggerLevelBytes (0 becomes 1) |
| `param_3` | `s32` | xIsMessageBuffer |
| `param_4` | `ptr` | pucStreamBufferStorageArea |
| `param_5` | `ptr` | StaticStreamBuffer_t *pxStaticStreamBuffer (0x24 bytes) |

**Returns** `ptr`: StreamBufferHandle_t = param_5, or NULL when no storage was given

**Notes:** Assert-style checks of stock FreeRTOS are compiled out; the NULL-storage check replaces them.

- Addresses by version: 219: 0x0C043498
- Called by: `ble_219_0c02e420`, `ble_219_0c0355c8`, `ble_219_0c04542c`
- Calls: `memset`
- Confidence: high

## xStreamBufferReceive

**FreeRTOS xStreamBufferReceive: read a stream or message from a buffer, blocking until data arrives**

Upstream xStreamBufferReceive(xStreamBuffer, pvRxData, xBufferLengthBytes, xTicksToWait). The wait for data lasts until more bytes are stored than the header size (4 for a message buffer, 0 for a stream); it uses xTaskNotifyWait on the waiting-receiver slot and the timeout-state helpers. For a message buffer the 4-byte length header is read first with prvReadBytesFromBuffer. If the message is longer than the caller's buffer the read pointer is rewound and 0 is returned, so the message stays queued. Otherwise the payload is read and the read pointer advanced. After a successful read a task waiting to send (xTaskWaitingToSend, +0x14) is notified with xTaskGenericNotify. Returns the payload bytes received. Part of the FreeRTOS stream buffer family in this packet.

| Parameter | Type | Description |
|---|---|---|
| `xStreamBuffer` | `ptr` | stream buffer handle |
| `pvRxData` | `ptr` | destination buffer |
| `xBufferLengthBytes` | `u32` | destination buffer size |
| `xTicksToWait` | `s32` | timeout in ticks |

**Returns** `u32`: payload bytes received; 0 when none or when the message does not fit

**Notes:** The message-too-large case rewinds the read pointer instead of dropping the message, which is what the decompile shows.

- Addresses by version: 219: 0x0C0436F8
- Called by: `ble_219_0c04264c`, `hci_stream_buffer_receive_nowait`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `prvReadBytesFromBuffer`, `vTaskSuspendAll`, `xTaskResumeAll`, `xTaskGetCurrentTaskHandle`, `xTaskNotifyWait`, `xTaskGenericNotify`, `xTaskNotifyStateClear`
- Confidence: high

## xStreamBufferReset

**FreeRTOS: empty a stream buffer if no task is blocked on it, keeping buffer, length, trigger level and number**

If xTaskWaitingToReceive (+0x10) or xTaskWaitingToSend (+0x14) is non-NULL returns pdFAIL (0). Otherwise saves pucBuffer (+0x18), xLength (+8), xTriggerLevelBytes (+0xC), ucFlags (+0x1C) and uxStreamBufferNumber (+0x20), memsets the 0x24-byte StreamBuffer_t to 0 and restores those fields, which resets xHead/xTail to 0. The flags byte is rebuilt as 1 if sbFLAGS_IS_MESSAGE_BUFFER was set and 0 otherwise, so the sbFLAGS_IS_STATIC bit (2) is dropped (harmless here because the image only creates static buffers and never deletes them). Returns pdPASS (1). No critical section around the check (differs from stock FreeRTOS). No direct callers (used through a function pointer / wrapper).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | StreamBufferHandle_t xStreamBuffer |
| `param_2` | `u32` | unused |
| `param_3` | `u32` | unused |
| `param_4` | `u32` | unused |

**Returns** `u32`: pdPASS (1) if reset, pdFAIL (0) if a task is blocked on the buffer

**Notes:** Corresponds to FreeRTOS 10.0.x xStreamBufferReset where the message-buffer flag is passed as a BaseType_t.

- Addresses by version: 219: 0x0C0434E8
- Calls: `memset`
- Confidence: high

## xStreamBufferSend

**FreeRTOS xStreamBufferSend: write a stream or message into a buffer, blocking for free space**

Upstream xStreamBufferSend(xStreamBuffer, pvTxData, xDataLengthBytes, xTicksToWait). For a message buffer (bit 0 of the flags byte at +0x1C) a 4-byte length header is added to the space needed. With a non-zero timeout it loops: while the free space is too small it clears the task notification state, records the timeout state and waits with xTaskNotifyWait, then rechecks. A message that still does not fit returns 0. It writes the optional 4-byte header and the payload with prvWriteBytesToBuffer, advances xHead, and when the stored count reaches the trigger level (+0x0C) notifies the waiting receiver (xTaskWaitingToReceive, +0x10) with xTaskGenericNotify. Returns the payload bytes written. Part of the FreeRTOS stream buffer family in this packet.

| Parameter | Type | Description |
|---|---|---|
| `xStreamBuffer` | `ptr` | stream buffer handle |
| `pvTxData` | `ptr` | source data |
| `xDataLengthBytes` | `u32` | payload length |
| `xTicksToWait` | `s32` | timeout in ticks |

**Returns** `u32`: payload bytes written, possibly 0

**Notes:** Counterpart of xStreamBufferSendFromISR (0x0C043658) described in an earlier wave.

- Addresses by version: 219: 0x0C043554
- Called by: `ble_219_0c0424d8`
- Calls: `vPortEnterCritical`, `vPortExitCritical`, `prvWriteBytesToBuffer`, `vTaskSuspendAll`, `xTaskResumeAll`, `vTaskSetTimeOutState`, `xTaskCheckForTimeOut`, `xTaskGetCurrentTaskHandle`, `xTaskNotifyWait`, `xTaskGenericNotify`, `xTaskNotifyStateClear`
- Confidence: high

## xStreamBufferSendFromISR

**FreeRTOS: copy data into a stream/message buffer from an ISR and wake the waiting reader**

FreeRTOS stream_buffer.c xStreamBufferSendFromISR(xStreamBuffer, pvTxData, xDataLengthBytes, pxHigherPriorityTaskWoken). StreamBuffer_t layout: [0]=xTail, [1]=xHead, [2]=xLength, [3]=xTriggerLevelBytes, [4]=xTaskWaitingToReceive, [5]=xTaskWaitingToSend, [6]=pucBuffer, byte +0x1c=ucFlags (bit0 = sbFLAGS_IS_MESSAGE_BUFFER). Free space = (xTail + xLength - 1 - xHead) mod xLength. For a message buffer the whole message plus a 4-byte length header must fit, otherwise 0 is returned; the header is written first with prvWriteBytesToBuffer (0x0c0433d0). For a plain stream buffer the write is truncated to the free space. After a non-empty write, if the bytes now stored ((xHead + xLength - xTail) mod xLength) reach xTriggerLevelBytes, the sbSEND_COMPLETE_FROM_ISR step runs under rtos_enter_critical/rtos_exit_critical: xTaskGenericNotifyFromISR(xTaskWaitingToReceive, 0, eNoAction, NULL, pxHigherPriorityTaskWoken) and the waiting-task slot is cleared. No critical section protects the buffer write itself (single-writer assumption). Returns the number of payload bytes written.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | StreamBuffer_t* handle |
| `param_2` | `ptr` | source data |
| `param_3` | `u32` | bytes to send |
| `param_4` | `ptr` | BaseType_t* pxHigherPriorityTaskWoken (may be NULL) |

**Returns** `u32`: bytes actually written (0 if a message did not fit)

- Addresses by version: 219: 0x0C043658
- Calls: `rtos_enter_critical`, `rtos_exit_critical`, `prvWriteBytesToBuffer`, `xTaskGenericNotifyFromISR`
- Confidence: high

## xTaskCheckForTimeOut

**FreeRTOS: test whether a blocking timeout expired and adjust the remaining ticks**

tasks.c xTaskCheckForTimeOut(pxTimeOut, pxTicksToWait), inside vPortEnterCritical/vPortExitCritical. First checks ucDelayAborted (pxCurrentTCB DAT_2000cb8c + 0x5e): if set it is cleared and pdTRUE returned (xTaskAbortDelay support). If *pxTicksToWait == portMAX_DELAY the result is pdFALSE (wait forever). If the overflow counter changed (pxTimeOut[0] != xNumOfOverflows DAT_2000cc5c) and xTickCount (DAT_2000cca0) already passed xTimeOnEntering, the timeout is pdTRUE. Else elapsed = xTickCount - xTimeOnEntering: if elapsed < *pxTicksToWait the remaining ticks are written back, the TimeOut_t is refreshed to now and pdFALSE returned; otherwise *pxTicksToWait = 0 and pdTRUE. Callers: queue send/receive/semaphore (0x0c042c8c, 0x0c042fa4, 0x0c0430a8, 0x0c043224) and stream-buffer receive (0x0c043554).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TimeOut_t* {xOverflowCount, xTimeOnEntering}, updated |
| `param_2` | `ptr` | TickType_t* ticks still to wait, updated in place |

**Returns** `bool`: pdTRUE if the timeout has expired

- Addresses by version: 219: 0x0C044378
- Called by: `xQueueGenericSend`, `xQueueReceive`, `xQueueSemaphoreTake`, `xQueuePeek`, `xStreamBufferSend`
- Calls: `vPortEnterCritical`, `vPortExitCritical`
- Confidence: high

## xTaskCreateStatic

**FreeRTOS xTaskCreateStatic: initialise a caller-supplied TCB and stack and make the task ready**

Upstream xTaskCreateStatic(pxTaskCode, pcName, ulStackDepth, pvParameters, uxPriority, puxStackBuffer, pxTaskBuffer). Returns NULL when either the TCB buffer or the stack buffer is NULL. Otherwise it stores the stack buffer in the TCB at +0x30 (pxStack), marks the TCB as statically allocated (ucStaticallyAllocated = 2 at +0x5D), initialises the task with prvInitialiseNewTask (0x0C043BA8) and adds it to the ready list with prvAddNewTaskToReadyList (0x0C043978). It returns the TCB handle. The two stack-passed arguments are recovered only partly in the decompile.

**Returns** `ptr`: task handle (the TCB), or NULL when a buffer is missing

**Notes:** Arguments are passed on the stack, so the decompile shows none. The +0x5D flag value follows the upstream constant and was not checked against this TCB layout.

- Addresses by version: 219: 0x0C043CFC
- Called by: `ble_219_0c02d724`, `ble_219_0c02e420`, `ble_219_0c0354e8`, `xTimerCreateTimerTask`, `ble_219_0c059a40`, `ble_bt_stack_task_create`
- Calls: `prvAddNewTaskToReadyList`, `prvInitialiseNewTask`
- Confidence: high

## xTaskGenericNotify

**FreeRTOS: send a task notification from task context and unblock the target**

tasks.c xTaskGenericNotify(xTaskToNotify, ulValue, eAction, pulPreviousNotificationValue) inside vPortEnterCritical/vPortExitCritical. Optionally returns the old ulNotifiedValue (+0x58), remembers the old ucNotifyState (+0x5c) and sets it to 2 (received). eAction: 1 eSetBits -> value |= ulValue; 2 eIncrement -> value++; 3 eSetValueWithOverwrite -> value = ulValue; 4 eSetValueWithoutOverwrite -> value = ulValue only if no notification was pending, otherwise returns pdFAIL (0); 0 eNoAction leaves the value. If the target was waiting (old state 1) it is removed from its blocked list (xStateListItem +4), uxTopReadyPriority (DAT_2000cc28) updated, appended to pxReadyTasksLists[uxPriority] (0x2000cb98 + prio*20) and rtos_pendsv_trigger issued when it outranks pxCurrentTCB (DAT_2000cb8c + 0x2c). Returns pdPASS otherwise. Callers: stream-buffer send/receive completion (0x0c043554, 0x0c0436f8, 0x0c043830, 0x0c0438d8).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TCB_t* task to notify |
| `param_2` | `u32` | ulValue |
| `param_3` | `u32` | eNotifyAction (0 none, 1 set bits, 2 increment, 3 overwrite, 4 no-overwrite) |
| `param_4` | `ptr` | uint32_t* previous value output (may be NULL) |

**Returns** `bool`: pdPASS, or pdFAIL when eSetValueWithoutOverwrite found a pending notification

- Addresses by version: 219: 0x0C044870
- Called by: `xStreamBufferSend`, `xStreamBufferReceive`, `stream_buffer_consume_tail`, `stream_buffer_commit_head`
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `vListInsertEnd`, `uxListRemove`
- Confidence: high

## xTaskGenericNotifyFromISR

**FreeRTOS: send a task notification from an ISR and flag a higher-priority wake-up**

tasks.c xTaskGenericNotifyFromISR(xTaskToNotify, ulValue, eAction, pulPreviousNotificationValue, pxHigherPriorityTaskWoken). Same value update as xTaskGenericNotify (eAction 1 set bits, 2 increment, 3 overwrite, 4 overwrite-only-if-idle returning pdFAIL otherwise) but protected with rtos_enter_critical/rtos_exit_critical (portSET/CLEAR_INTERRUPT_MASK_FROM_ISR). If the target was waiting (ucNotifyState +0x5c == 1): when the scheduler is running (uxSchedulerSuspended DAT_2000cc20 == 0) the task is moved from its blocked list to pxReadyTasksLists[uxPriority] (0x2000cb98 + prio*20, uxTopReadyPriority DAT_2000cc28 updated); otherwise its xEventListItem (+0x18) is parked on xPendingReadyList (0x2000cc60). If the woken task outranks pxCurrentTCB, *pxHigherPriorityTaskWoken = pdTRUE when the pointer is given, else xYieldPending (DAT_2000cca4) is set. Callers: xStreamBufferSendFromISR and the ISR send/receive-completed helpers 0x0c043830, 0x0c0438d8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TCB_t* task to notify |
| `param_2` | `u32` | ulValue |
| `param_3` | `u32` | eNotifyAction (0..4) |
| `param_4` | `ptr` | uint32_t* previous value output (may be NULL) |
| `param_5` | `ptr` | BaseType_t* pxHigherPriorityTaskWoken (may be NULL) |

**Returns** `bool`: pdPASS, or pdFAIL for eSetValueWithoutOverwrite with a pending notification

- Addresses by version: 219: 0x0C044914
- Called by: `xStreamBufferSendFromISR`, `stream_buffer_consume_tail`, `stream_buffer_commit_head`
- Calls: `rtos_enter_critical`, `rtos_exit_critical`, `vListInsertEnd`, `uxListRemove`
- Confidence: high

## xTaskGetCurrentTaskHandle

**FreeRTOS: return pxCurrentTCB**

Returns the current TCB pointer DAT_2000cb8c (the running task's handle). Eight callers in the task/queue code.

**Returns** `ptr`: handle of the running task

- Addresses by version: 219: 0x0C04462C
- Called by: `ble_219_0c0360d4`, `hal_wdt_task_checkin`, `ble_219_0c036328`, `xQueueGiveMutexRecursive`, `rtos_mutex_give_checked`, `xQueueTakeMutexRecursive`, `xStreamBufferSend`, `xStreamBufferReceive`
- Confidence: high

## xTaskGetSchedulerState

**FreeRTOS: report scheduler not-started / running / suspended**

If xSchedulerRunning (DAT_2000cc74) is 0 returns 1 (taskSCHEDULER_NOT_STARTED); else if uxSchedulerSuspended (DAT_2000cc20) is 0 returns 2 (taskSCHEDULER_RUNNING), otherwise 0 (taskSCHEDULER_SUSPENDED).

**Returns** `u32`: 0 = suspended, 1 = not started, 2 = running

- Addresses by version: 219: 0x0C044638
- Called by: `ble_219_0c035900`, `xTimerGenericCommand`, `ble_stack_lock_take`, `ble_stack_lock_give`
- Confidence: high

## xTaskGetTickCount

**FreeRTOS: return the current tick count**

Returns xTickCount (DAT_2000cca0). Same variable is stored in a TimeOut_t by vTaskInternalSetTimeOutState. Used widely (many callers) for timeouts and timestamps.

**Returns** `u32`: tick count (ticks)

- Addresses by version: 219: 0x0C043F1C
- Called by: `ble_219_0c0285ec`, `ble_219_0c0297b0`, `ble_219_0c029df8`, `ble_219_0c02b480`, `ble_219_0c02e7d8`, `ble_219_0c02eb60`, `ble_219_0c0369d8`, `ble_219_0c037588`, `ble_219_0c037970`, `ble_219_0c03be8c`, `clock_gettime`, `gettimeofday` ...
- Confidence: high

## xTaskIncrementTick

**FreeRTOS: advance xTickCount, unblock expired delayed tasks and report whether to switch**

tasks.c xTaskIncrementTick(), called from the SysTick handler (0x0c03f674) and from xTaskResumeAll for pended ticks. If uxSchedulerSuspended (DAT_2000cc20) is non-zero it only increments uxPendedTicks (DAT_2000cc1c) and still calls the (empty) vApplicationTickHook ble_stub_nop_0c047fe8. Otherwise xTickCount (DAT_2000cca0) is incremented; on wrap to 0 the delayed lists are swapped (pxDelayedTaskList DAT_2000cb90 <-> pxOverflowDelayedTaskList DAT_2000cb94), xNumOfOverflows (DAT_2000cc5c) incremented and xNextTaskUnblockTime (DAT_2000cc58) recomputed from the new list head. When the tick reaches xNextTaskUnblockTime every task at the head of pxDelayedTaskList whose item value <= tick is removed (uxListRemove on xStateListItem, and on xEventListItem +0x18 if its container +0x28 is set), uxTopReadyPriority (DAT_2000cc28) is updated and the task appended to pxReadyTasksLists[priority] (0x2000cb98 + prio*20); xSwitchRequired is set if its priority >= that of pxCurrentTCB. With time slicing, a switch is also requested when the ready list of the current priority holds more than one task. The tick hook is only invoked when no ticks were pended. Finally xYieldPending (DAT_2000cca4) forces a pdTRUE result.

**Returns** `bool`: pdTRUE when a context switch should be performed

- Addresses by version: 219: 0x0C043F48
- Called by: `SysTick_Handler`, `xTaskResumeAll`
- Calls: `vListInsertEnd`, `uxListRemove`, `ble_stub_nop_0c047fe8`
- Confidence: high

## xTaskNotifyStateClear

**FreeRTOS: clear a pending notification state of a task (or the current task)**

tasks.c xTaskNotifyStateClear(xTask). A NULL handle means pxCurrentTCB (DAT_2000cb8c). Inside vPortEnterCritical/vPortExitCritical: if ucNotifyState (+0x5c) == 2 (notification received) it is reset to 0 and pdTRUE returned, otherwise pdFALSE. The notification value itself is untouched. Callers: the stream-buffer blocking paths 0x0c043554 and 0x0c0436f8 (sbRECEIVE_COMPLETED / sbSEND_COMPLETED housekeeping).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TaskHandle_t, NULL for the calling task |

**Returns** `bool`: pdTRUE if a pending notification was cleared

- Addresses by version: 219: 0x0C0449FC
- Called by: `xStreamBufferSend`, `xStreamBufferReceive`
- Calls: `vPortEnterCritical`, `vPortExitCritical`
- Confidence: high

## xTaskNotifyWait

**FreeRTOS: wait for a task notification, clearing bits on entry and exit**

tasks.c xTaskNotifyWait(ulBitsToClearOnEntry, ulBitsToClearOnExit, pulNotificationValue, xTicksToWait) operating on pxCurrentTCB (DAT_2000cb8c): ulNotifiedValue at +0x58, ucNotifyState at +0x5c (0 = not waiting, 1 = waiting, 2 = notification received). First critical section (vPortEnterCritical/vPortExitCritical 0x0c03f640/0x0c03f65c): if no notification is pending, clears the entry bits, sets state = waiting and, if xTicksToWait != 0, calls prvAddCurrentTaskToDelayedList and rtos_pendsv_trigger to block. Second critical section after wake-up: optionally returns the value through pulNotificationValue, returns pdTRUE if state == received (clearing the exit bits), pdFALSE on timeout, and resets the state to not-waiting. Callers: the stream-buffer send/receive blocking paths 0x0c043554 and 0x0c0436f8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | ulBitsToClearOnEntry |
| `param_2` | `u32` | ulBitsToClearOnExit |
| `param_3` | `ptr` | uint32_t* pulNotificationValue output (may be NULL) |
| `param_4` | `u32` | xTicksToWait (ticks) |

**Returns** `bool`: pdTRUE if a notification was received, pdFALSE on timeout

- Addresses by version: 219: 0x0C0447E8
- Called by: `xStreamBufferSend`, `xStreamBufferReceive`
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `prvAddCurrentTaskToDelayedList`
- Confidence: high

## xTaskPriorityDisinherit

**FreeRTOS: drop an inherited priority when the last held mutex is released**

tasks.c xTaskPriorityDisinherit(pxMutexHolder). Returns 0 for a NULL holder. Decrements uxMutexesHeld (+0x50); if the task runs at an inherited priority (uxPriority +0x2c != uxBasePriority +0x4c) and now holds no mutexes, it is removed from its ready list, xEventListItem.xItemValue (+0x18) is reset to 6 - base priority, uxPriority restored to the base priority, uxTopReadyPriority (DAT_2000cc28) updated and the task appended to pxReadyTasksLists[base] (0x2000cb98 + prio*20); returns pdTRUE so the caller yields. Called from the mutex give path 0x0c042a3c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TCB_t* mutex holder (may be NULL) |

**Returns** `bool`: pdTRUE if the holder's priority was lowered

- Addresses by version: 219: 0x0C0446E4
- Called by: `prvCopyDataToQueue`
- Calls: `vListInsertEnd`, `uxListRemove`
- Confidence: high

## xTaskPriorityInherit

**FreeRTOS: raise a mutex holder's priority to that of the current task**

tasks.c xTaskPriorityInherit(pxMutexHolder). Returns pdFALSE for a NULL holder. If the holder's uxPriority (+0x2c) is already >= pxCurrentTCB's, it returns whether uxBasePriority (+0x4c) < current priority (i.e. an inheritance already happened). Otherwise it inherits: if xEventListItem.xItemValue (+0x18) is not flagged in-use (bit 31 clear) it is set to 6 - current priority; if the holder sits in its ready list (xStateListItem container +0x14 == &pxReadyTasksLists[old prio]) it is moved to pxReadyTasksLists[new prio] (0x2000cb98 + prio*20, uxTopReadyPriority DAT_2000cc28 updated), otherwise only uxPriority is rewritten. Returns pdTRUE when the priority changed. Caller: the semaphore/mutex take path 0x0c0430a8 when the mutex is held by a lower-priority task.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | TCB_t* current mutex holder (may be NULL) |

**Returns** `bool`: pdTRUE if priority inheritance occurred

- Addresses by version: 219: 0x0C044658
- Called by: `xQueueSemaphoreTake`
- Calls: `vListInsertEnd`, `uxListRemove`
- Confidence: high

## xTaskRemoveFromEventList

**FreeRTOS: wake the highest-priority task blocked on an event list**

tasks.c xTaskRemoveFromEventList(pxEventList). Takes the TCB owning the head entry (list +0xc -> item, item +0xc -> owner), removes its xEventListItem (+0x18). If the scheduler is running (uxSchedulerSuspended DAT_2000cc20 == 0) it also removes the xStateListItem (+4) from the delayed list, updates uxTopReadyPriority (DAT_2000cc28) and appends the task to pxReadyTasksLists[uxPriority] (0x2000cb98 + prio*20); otherwise the event item is parked on xPendingReadyList (0x2000cc60) for xTaskResumeAll. Returns pdTRUE and sets xYieldPending (DAT_2000cca4) when the woken task has a higher priority than pxCurrentTCB (DAT_2000cb8c + 0x2c). Called from the queue/semaphore code (8 callers) after data or space becomes available.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | List_t* event list (xTasksWaitingToSend/Receive) |

**Returns** `bool`: pdTRUE if the unblocked task should pre-empt the caller

- Addresses by version: 219: 0x0C044264
- Called by: `prvUnlockQueue`, `xQueueGenericReset`, `xQueueGenericSend`, `xQueueGenericSendFromISR`, `xQueueGiveFromISR`, `xQueueReceive`, `xQueueSemaphoreTake`, `xQueuePeek`
- Calls: `vListInsertEnd`, `uxListRemove`
- Confidence: high

## xTaskResumeAll

**FreeRTOS: resume the scheduler, drain the pending-ready list and replay pended ticks**

tasks.c xTaskResumeAll(). Inside vPortEnterCritical/vPortExitCritical (0x0c03f640/0x0c03f65c) decrements uxSchedulerSuspended (DAT_2000cc20). When it reaches 0 and tasks exist (uxCurrentNumberOfTasks DAT_2000cc14 != 0): every task in xPendingReadyList (0x2000cc60, head owner via +0xc) is unlinked from both its xEventListItem (+0x18) and xStateListItem (+4) and appended to pxReadyTasksLists[uxPriority] (0x2000cb98 + prio*20), raising uxTopReadyPriority (DAT_2000cc28) and setting xYieldPending (DAT_2000cca4) when the task's priority >= pxCurrentTCB->uxPriority; xNextTaskUnblockTime (DAT_2000cc58) is reset from the head of pxDelayedTaskList (DAT_2000cb90) or to portMAX_DELAY. Then uxPendedTicks (DAT_2000cc1c) ticks are replayed by calling xTaskIncrementTick that many times. If a yield is pending, rtos_pendsv_trigger is called and pdTRUE returned (the caller already switched). Pairs with vTaskSuspendAll; used by queue, timer, event-group and notification code (many callers).

**Returns** `bool`: pdTRUE if a context switch was requested, else pdFALSE

- Addresses by version: 219: 0x0C0440AC
- Called by: `xEventGroupWaitBits`, `xEventGroupSetBits`, `xQueueGenericSend`, `xQueueReceive`, `xQueueSemaphoreTake`, `xQueuePeek`, `xStreamBufferSend`, `xStreamBufferReceive`, `stream_buffer_consume_tail`, `stream_buffer_commit_head`, `vTaskDelay`, `vTaskGetInfo` ...
- Calls: `rtos_pendsv_trigger`, `vPortEnterCritical`, `vPortExitCritical`, `vListInsertEnd`, `uxListRemove`, `xTaskIncrementTick`
- Confidence: high

## xTimerCreateTimerTask

**Create the 'Tmr Svc' FreeRTOS timer daemon task (static, depth 0x400, priority 5)**

Upstream xTimerCreateTimerTask. It makes sure the timer lists and command queue exist through prvCheckForValidListAndQueue (0x0C044AA4), then creates the timer service task statically with xTaskCreateStatic (0x0C043CFC). The entry point is 0x0C044EE8 (prvTimerTask), name 'Tmr Svc', stack depth 0x400, no parameter, priority 5, stack at 0x2000CCB0 and TCB at 0x2000DCB0. The task handle is stored in DAT_2000DE24, and the function returns true only when the task was created.

**Returns** `bool`: true when the timer task was created

- Addresses by version: 219: 0x0C044C2C
- Called by: `ble_219_0c043e70`
- Calls: `xTaskCreateStatic`, `prvCheckForValidListAndQueue`
- Confidence: high

## xTimerGenericCommand

**FreeRTOS xTimerGenericCommand: post a command to the timer daemon queue from task or ISR context**

Upstream xTimerGenericCommand(xTimer, xCommandID, xOptionalValue, pxHigherPriorityTaskWoken, xTicksToWait). It returns 0 when the command queue DAT_2000DE20 does not exist. It builds a message on the stack. Task-context commands (id below 6, tmrFIRST_FROM_ISR_COMMAND) go through xQueueGenericSend. The timeout is used only when the scheduler is running (xTaskGetSchedulerState 2); before that the send uses zero wait. ISR-style commands (id 6 and above, including the -2 callback id) go through xQueueGenericSendFromISR with pxHigherPriorityTaskWoken.

| Parameter | Type | Description |
|---|---|---|
| `xTimer` | `ptr` | timer handle |
| `xCommandID` | `s32` | timer command id |
| `xOptionalValue` | `u32` | command value, for example the new expiry |
| `pxHigherPriorityTaskWoken` | `ptr` | used for ISR-style commands |
| `xTicksToWait` | `u32` | timeout in ticks for task-context commands |

**Returns** `s32`: 1 when the command was queued, 0 on failure

- Addresses by version: 219: 0x0C044D90
- Called by: `ble_219_0c0297b0`, `ble_219_0c03be8c`, `bt_drv_pending_action_poll`, `prvSwitchTimerLists`, `ble_219_0c044ee8`, `ble_219_0c059180`
- Calls: `xQueueGenericSend`, `xQueueGenericSendFromISR`, `xTaskGetSchedulerState`
- Confidence: high
