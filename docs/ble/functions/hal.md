# BLE - `hal` functions

167 functions.

| Function | Address (BLE_219) | Summary |
|---|---|---|
| [`analogif_reg3037_3048_config`](#analogif_reg3037_3048_config) | 0x0C086C30 | Read-modify-write analog registers 0x3037 (clear bits 7-8) and 0x3048 (set bit 13) |
| [`analogif_reg30b7_channel_read`](#analogif_reg30b7_channel_read) | 0x0C086B04 | Sequence writes to analog register 0x30B7 to sample channel N and read the result from 0x30BE\|0x30BD |
| [`bes_analog_clock_mode_config`](#bes_analog_clock_mode_config) | 0x0C03C30C | Program analog/clock config registers 0xD0220C18 and 0xD0220C90 for mode 2, 3 or default |
| [`bes_analog_init_defaults`](#bes_analog_init_defaults) | 0x0C03C7B0 | Initialise four registers in the 0xD0220C0C..0xD0220C8C analog block |
| [`bes_analog_set_c10_field`](#bes_analog_set_c10_field) | 0x0C03C470 | Enable (with a 4-bit value) or disable a field in register 0xD0220C10 |
| [`bes_aon_reg38_staged_release`](#bes_aon_reg38_staged_release) | 0x0C041A68 | Write the 0xCAFE02xx key sequence FF->F7->F3->F1->F0 to 0x40085038 with delays |
| [`bes_calib_get_trim_pair`](#bes_calib_get_trim_pair) | 0x0C03A1B0 | Return two 16-bit calibration words: defaults, or OTP trims plus 12000 and 16200 |
| [`bes_cmu_bit29_ctrl`](#bes_cmu_bit29_ctrl) | 0x0C040CD0 | Write bit 29 to the 0x40000060 (param=0) or 0x40000064 (param!=0) register |
| [`bes_cmu_bit30_ctrl`](#bes_cmu_bit30_ctrl) | 0x0C040CE8 | Write bit 30 to the 0x40000060 (param=0) or 0x40000064 (param!=0) register |
| [`bes_cmu_reg5c_clear_bit9`](#bes_cmu_reg5c_clear_bit9) | 0x0C0409E4 | Clear bit 9 of peripheral register 0x4000005c under BASEPRI lock |
| [`bes_cmu_reg5c_set_bit10`](#bes_cmu_reg5c_set_bit10) | 0x0C040A20 | Set bit 10 of peripheral register 0x4000005c under BASEPRI lock |
| [`bes_cmu_set_reg70_sel_b12`](#bes_cmu_set_reg70_sel_b12) | 0x0C040E08 | Clear or set a selector field in 0x40000070 (0 = clear, 1 = set), under BASEPRI lock |
| [`bes_cmu_set_reg70_sel_b2`](#bes_cmu_set_reg70_sel_b2) | 0x0C040D58 | Clear or set a selector field in 0x40000070 (0 = clear, 1 = set), under BASEPRI lock |
| [`bes_cmu_set_reg70_sel_b7`](#bes_cmu_set_reg70_sel_b7) | 0x0C040DB0 | Clear or set a selector field in 0x40000070 (0 = clear, 1 = set), under BASEPRI lock |
| [`bes_cmu_set_reg74_sel_b3`](#bes_cmu_set_reg74_sel_b3) | 0x0C040EC0 | Clear or set a selector field in 0x40000074 (0 = clear, 1 = set), under BASEPRI lock |
| [`bes_cmu_set_rega8_bit21`](#bes_cmu_set_rega8_bit21) | 0x0C040F18 | Clear (0) or set (1) bit 21 of 0x400000a8 under BASEPRI lock |
| [`bes_cmu_set_sysclk_cfg`](#bes_cmu_set_sysclk_cfg) | 0x0C040BC8 | Apply clock-gate enable/disable masks for a system-clock configuration index 0..7 |
| [`bes_cmu_set_sysclk_mode`](#bes_cmu_set_sysclk_mode) | 0x0C040BBC | Store the clock-switch mode byte used by bes_cmu_set_sysclk_cfg |
| [`bes_cmu_stub_return_0`](#bes_cmu_stub_return_0) | 0x0C040CCC | Stub that returns 0 |
| [`bes_gpio_mask_clear`](#bes_gpio_mask_clear) | 0x0C041B20 | Clear bit for pin 0..35 in the mask words 0x40085080 (0-31) / 0x40085084 (32-35) |
| [`bes_gpio_mask_set`](#bes_gpio_mask_set) | 0x0C041AE8 | Set bit for pin 0..35 in the mask words 0x40085080 (0-31) / 0x40085084 (32-35) |
| [`bes_gpio_read_status_words`](#bes_gpio_read_status_words) | 0x0C041AB0 | Copy up to three 32-bit status words from 0x4008508c/90/94 into a buffer |
| [`bes_hw_get_const_4000`](#bes_hw_get_const_4000) | 0x0C041328 | Return the constant 4000 |
| [`bes_hw_init_clock_power_regs`](#bes_hw_init_clock_power_regs) | 0x0C04110C | Write the default configuration of the clock/power and system register blocks at boot |
| [`bes_hw_nop_hook`](#bes_hw_nop_hook) | 0x0C0410E4 | Empty hook function (bx lr) |
| [`bes_iomux_apply_default_pin_cfg`](#bes_iomux_apply_default_pin_cfg) | 0x0C041638 | For all 36 pins whose function nibble is 0xf, clear a bit in one register and set it in another |
| [`bes_iomux_get_pin_table_entry`](#bes_iomux_get_pin_table_entry) | 0x0C041A00 | Look up a byte in the 36x6 pin table at 0x0c08355c |
| [`bes_iomux_init_level2`](#bes_iomux_init_level2) | 0x0C041884 | Program the 0x40086000 block to level 2 and then clear bits 19:18 of 0x4008602c and 0x40086030 |
| [`bes_iomux_reg0c_set_level`](#bes_iomux_reg0c_set_level) | 0x0C0414E0 | Under lock, wait for the 0x40086000 block to be idle and program nibbles 11:8 and 15:12 of 0x4008600c to param_1 |
| [`bes_iomux_reg44_clear_bits`](#bes_iomux_reg44_clear_bits) | 0x0C0418F4 | Clear bits in 0x40086044 and return the previous low 16 bits |
| [`bes_iomux_reg44_set_bits`](#bes_iomux_reg44_set_bits) | 0x0C0418E0 | Set bits in 0x40086044 and return the previous low 16 bits |
| [`bes_otp_load_variant`](#bes_otp_load_variant) | 0x0C0385FC | Load a 2-bit hardware variant from OTP word 0xC into DAT_20003D64 |
| [`bes_pack_two_14bit_fields`](#bes_pack_two_14bit_fields) | 0x0C03EF58 | Pack two 14-bit values into a 32-bit register image and clear bit 31 of 0xD0350250 |
| [`bes_periph_d033_config`](#bes_periph_d033_config) | 0x0C03CD38 | Clear bit 7 of 0xD0330038 and set bit 18 / clear bit 5 of 0xD0330024 |
| [`bes_periph_d035_init_main`](#bes_periph_d035_init_main) | 0x0C03CA04 | Big one-shot initialisation of the 0xD0350xxx register block, including two RAM buffer pointers |
| [`bes_periph_d035_init_small`](#bes_periph_d035_init_small) | 0x0C03C87C | Initialise six registers in the 0xD0350240..0xD035035C block |
| [`bes_rf_set_mode_bits`](#bes_rf_set_mode_bits) | 0x0C03BE88 | Set the 2-bit field at bits 13..14 of RF register 0xD0220C7C, bracketed by sysreg gates |
| [`bes_rf_synth_config_by_mode`](#bes_rf_synth_config_by_mode) | 0x0C03C380 | Set fields in 0xD0350xxx registers for mode 0 or 1; hangs on any other value |
| [`bes_sysreg_ack_pending_bit8`](#bes_sysreg_ack_pending_bit8) | 0x0C041330 | Write 0x4000000 to 0x40080040 and 0x100 to 0x40080004, with read-backs of 0x40080000 |
| [`bes_sysreg_cfg_step2`](#bes_sysreg_cfg_step2) | 0x0C041348 | Reconfigure fields of 0x40080090/0x400800b0/0x4008003c then trigger via 0x40080014 and 0x400800cc |
| [`bes_sysreg_cfg_step3`](#bes_sysreg_cfg_step3) | 0x0C0413C4 | Set field 0x82 in bits 15..8 of 0x4008006c and set bit 27 of 0x40080084 |
| [`bes_sysreg_read_80000_hi16`](#bes_sysreg_read_80000_hi16) | 0x0C0413E4 | Return the upper 16 bits of peripheral register 0x40080000 |
| [`bes_sysreg_select_mode1`](#bes_sysreg_select_mode1) | 0x0C0410E8 | Set the low 3-bit field of 0x4008005c and 0x400800b4 to 1 |
| [`bes_sysreg_set_f8_low_byte`](#bes_sysreg_set_f8_low_byte) | 0x0C04124C | Replace the low byte of peripheral register 0x400800f8 |
| [`bes_sysreg_write_04_bit19`](#bes_sysreg_write_04_bit19) | 0x0C0413F0 | Write bit 19 to 0x40080004 under BASEPRI lock, then read back 0x40080000 |
| [`bes_sysreg_write_04_bit4`](#bes_sysreg_write_04_bit4) | 0x0C0410B8 | Write 0x10 to peripheral register 0x40080004 |
| [`bes_sysreg_write_08_bit19`](#bes_sysreg_write_08_bit19) | 0x0C041430 | Write bit 19 to 0x40080008 under BASEPRI lock |
| [`ble_hw_ctrl_reg_bit1_clear`](#ble_hw_ctrl_reg_bit1_clear) | 0x0C08665C | If param_1 == 0, clear bit 1 of the register at 0x07FFA000; return 0 |
| [`ble_hw_ctrl_reg_bit1_set`](#ble_hw_ctrl_reg_bit1_set) | 0x0C086648 | If param_1 == 0, set bit 1 of the register at 0x07FFA000; return 0 |
| [`ble_ring_dispatch_pending`](#ble_ring_dispatch_pending) | 0x0C048B00 | Drain a ring of queued callbacks until the read index meets the write index |
| [`flash_cache_hook_nop_a`](#flash_cache_hook_nop_a) | 0x0C086BB8 | Empty stub (immediate return) |
| [`flash_cache_hook_nop_b`](#flash_cache_hook_nop_b) | 0x0C086BBC | Empty stub (immediate return) |
| [`hal_analogif_reg_read`](#hal_analogif_reg_read) | 0x0C0401B0 | Read a 16-bit analog/PMU/RF register over the internal SPI (ISPI) with page selection |
| [`hal_analogif_reg_write`](#hal_analogif_reg_write) | 0x0C040290 | Write a 16-bit analog/PMU/RF register over the internal SPI (ISPI) with page selection |
| [`hal_block_40008000_open`](#hal_block_40008000_open) | 0x0C0332B4 | Open the 0x40008000 block: enable clock and reset 0x28, program rate and mode, cache both |
| [`hal_block_40008000_open_default`](#hal_block_40008000_open_default) | 0x0C04584C | Open the 0x40008000 peripheral with the constant configuration at 0x0c081040 |
| [`hal_block_40008000_set_run`](#hal_block_40008000_set_run) | 0x0C03324C | Start or stop the 0x40008000 block: reload mode and rate when ready, set run register |
| [`hal_cache_enable`](#hal_cache_enable) | 0x0C02ED04 | Enable the cache controller at 0x07FFA000 (id 0), or pend a request if already on |
| [`hal_chip_select_cfg_word`](#hal_chip_select_cfg_word) | 0x0C02ED5C | Select one of two 32-bit constants from a ROM table into DAT_20003540 |
| [`hal_cmu_aonclk9_user_disable`](#hal_cmu_aonclk9_user_disable) | 0x0C0414AC | Reference-counted disable of AON-CMU clock bit 9 (0x40080008 = 0x200) for user 0..3 |
| [`hal_cmu_aonclk9_user_enable`](#hal_cmu_aonclk9_user_enable) | 0x0C04146C | Reference-counted enable of AON-CMU clock bit 9 (0x40080004 = 0x200) for user 0..3 |
| [`hal_cmu_clk_block_8c_enable`](#hal_cmu_clk_block_8c_enable) | 0x0C041264 | Configure and power up the clock block controlled by 0x4000008c in one of three modes (0..2) |
| [`hal_cmu_clock_disable`](#hal_cmu_clock_disable) | 0x0C04070C | Disable the clock/gate for module id n by writing its bit to a clear register |
| [`hal_cmu_clock_enable`](#hal_cmu_clock_enable) | 0x0C040690 | Enable the clock/gate for module id n by writing its bit to a set register |
| [`hal_cmu_clock_is_enabled`](#hal_cmu_clock_is_enabled) | 0x0C040784 | Return whether the clock/gate bit of module id n is currently set |
| [`hal_cmu_get_crystal_freq`](#hal_cmu_get_crystal_freq) | 0x0C02ED78 | Return the nominal crystal frequency, 24000000 Hz |
| [`hal_cmu_osc_x2_enable`](#hal_cmu_osc_x2_enable) | 0x0C0410C4 | Power up the crystal x2 clock (0x40000060 = 0x4000), wait 60 us, then enable it (0x2000) |
| [`hal_cmu_pll_enable`](#hal_cmu_pll_enable) | 0x0C0404AC | Power up and enable PLL 0..2 for a user id with reference counting in DAT_20003D84[] |
| [`hal_cmu_pll_release_user`](#hal_cmu_pll_release_user) | 0x0C0405F4 | Clear a user bit for clock source n and power it down when the last user is gone |
| [`hal_cmu_reset_clear`](#hal_cmu_reset_clear) | 0x0C040890 | Release (clear) the reset bit of module id n |
| [`hal_cmu_reset_get_state`](#hal_cmu_reset_get_state) | 0x0C0403C8 | Test whether the reset/gate bit of module id n is set in the 0x40000034.. status registers |
| [`hal_cmu_reset_pulse`](#hal_cmu_reset_pulse) | 0x0C04092C | Range-check a CMU module id (<= 0x99) and pulse its reset line |
| [`hal_cmu_reset_pulse_nocheck`](#hal_cmu_reset_pulse_nocheck) | 0x0C040934 | Pulse the software reset of CMU module id (no range check), or release it if currently held in reset |
| [`hal_cmu_reset_set`](#hal_cmu_reset_set) | 0x0C040804 | Assert (set) the reset bit of module id n |
| [`hal_cmu_reset_set_mod99`](#hal_cmu_reset_set_mod99) | 0x0C02ED80 | Assert the CMU software reset of module id 0x99 (bit 8 of 0x400800c8) |
| [`hal_cmu_select_pll_source`](#hal_cmu_select_pll_source) | 0x0C040450 | Record the active clock source index and program bits 18:17 of 0x40000070 inside a critical section |
| [`hal_cmu_sys_pll_restart`](#hal_cmu_sys_pll_restart) | 0x0C040CFC | Release all users of PLL 0, reselect source 0, clear 0x4000010c bits 31:30 and re-enable PLL 0 |
| [`hal_ext_ctrl_write_d0702000`](#hal_ext_ctrl_write_d0702000) | 0x0C03AA64 | Write 1 and 2 to the two control words at 0xd0702000/0xd0702004 |
| [`hal_gpadc_adc2volt`](#hal_gpadc_adc2volt) | 0x0C02F810 | Convert a raw GPADC code to a calibrated voltage (two-point calibration from efuse, lazily initialised) |
| [`hal_gpdma_cancel`](#hal_gpdma_cancel) | 0x0C02F354 | Stop a GPDMA channel and clear its pending interrupt flags |
| [`hal_gpdma_chan_busy`](#hal_gpdma_chan_busy) | 0x0C02F5DC | Return whether a GPDMA channel is currently enabled/running |
| [`hal_gpdma_chan_irq_handler`](#hal_gpdma_chan_irq_handler) | 0x0C02EECC | Service one GPDMA channel interrupt: clear TC/error flags and invoke the user callback |
| [`hal_gpdma_free_chan`](#hal_gpdma_free_chan) | 0x0C02F558 | Cancel a GPDMA channel and release it (clear allocation flag and its sync bit in the controller config) |
| [`hal_gpdma_get_chan`](#hal_gpdma_get_chan) | 0x0C02F41C | Allocate a free GPDMA channel for a peripheral |
| [`hal_gpdma_get_sg_remain_size`](#hal_gpdma_get_sg_remain_size) | 0x0C02F610 | Return the total number of units still to transfer on a GPDMA channel |
| [`hal_gpdma_init`](#hal_gpdma_init) | 0x0C02F6A4 | One-time initialisation of both GPDMA controllers |
| [`hal_gpdma_init_desc`](#hal_gpdma_init_desc) | 0x0C02EF3C | Fill a 4-word GPDMA linked-list descriptor from a channel configuration |
| [`hal_gpdma_sg_start`](#hal_gpdma_sg_start) | 0x0C02F098 | Program a GPDMA channel with a descriptor and config, then start it |
| [`hal_gpdma_sg_start_linear`](#hal_gpdma_sg_start_linear) | 0x0C02F328 | Start a scatter-gather GPDMA transfer without 2-D descriptors (hal_gpdma_sg_start(desc, cfg, NULL)) |
| [`hal_gpdma_start`](#hal_gpdma_start) | 0x0C02F330 | Start a single-descriptor GPDMA transfer from a channel configuration |
| [`hal_gpdma_stop`](#hal_gpdma_stop) | 0x0C02F390 | Halt a GPDMA channel, wait (up to 10 tries) for it to go inactive, then cancel it |
| [`hal_hwsem_try_lock`](#hal_hwsem_try_lock) | 0x0C0319DC | Read hardware semaphore register n (0..3) at 0x400000C0 |
| [`hal_hwsem_unlock`](#hal_hwsem_unlock) | 0x0C0319F0 | Write 1 to hardware semaphore register n (0..3) at 0x400000C0 to release it |
| [`hal_i2c_calc_scl_cnt`](#hal_i2c_calc_scl_cnt) | 0x0C030368 | Compute SCL high/low counts for an I2C bus speed from timing minima |
| [`hal_i2c_check_tx_abort`](#hal_i2c_check_tx_abort) | 0x0C0302B4 | Check I2C raw error status and prepare the controller to recover from a TX abort |
| [`hal_i2c_clear_busy`](#hal_i2c_clear_busy) | 0x0C030268 | Clear an I2C instance's bit in the busy mask DAT_2000a6c8; drop PM busy bit 2 when none remain |
| [`hal_i2c_close_internal`](#hal_i2c_close_internal) | 0x0C030A08 | Close an I2C instance: disable its NVIC IRQ and controller, clear busy, assert resets and gate clocks |
| [`hal_i2c_master_recv_poll`](#hal_i2c_master_recv_poll) | 0x0C030CB8 | Polled I2C master read of n bytes, keeping the 8-deep FIFO filled with READ commands |
| [`hal_i2c_master_send_poll`](#hal_i2c_master_send_poll) | 0x0C030AB0 | Polled I2C master write of n bytes with optional RESTART/STOP flags and timeouts |
| [`hal_i2c_recv`](#hal_i2c_recv) | 0x0C03136C | Exported I2C write-then-read: send the register/command bytes, then read rx_len bytes with RESTART+STOP |
| [`hal_i2c_send`](#hal_i2c_send) | 0x0C03134C | Exported I2C write: assert instance < 6 and tail-call hal_i2c_master_send_poll with all arguments |
| [`hal_i2c_task_done_handler`](#hal_i2c_task_done_handler) | 0x0C030198 | I2C completion handler: invoke the callback of the finished task and advance the 2-entry task ring |
| [`hal_i2c_task_start_next`](#hal_i2c_task_start_next) | 0x0C030428 | Kick the next queued interrupt-mode I2C task of an instance: program TAR/thresholds, unmask IRQs, enable |
| [`hal_init_stub_ret0_a`](#hal_init_stub_ret0_a) | 0x0C02ED24 | Stub returning 0, called from the platform init routine |
| [`hal_init_stub_ret0_b`](#hal_init_stub_ret0_b) | 0x0C02ED28 | Second stub returning 0, called from the platform init routine |
| [`hal_irq_get_handler_table`](#hal_irq_get_handler_table) | 0x0C0342B8 | Return the base address of the RAM handler table at 0x2000aa80 |
| [`hal_periph_9000_set_field_10_7`](#hal_periph_9000_set_field_10_7) | 0x0C0326A8 | Set a 4-bit field (bits 10:7) in the register at 0x40009004 |
| [`hal_pmu_get_saved_status_nibble`](#hal_pmu_get_saved_status_nibble) | 0x0C02ECD8 | Return the status nibble saved from register 0x40080038 |
| [`hal_pmu_save_and_clear_status_nibble`](#hal_pmu_save_and_clear_status_nibble) | 0x0C02ECE4 | Save low 4 bits of reg 0x40080038 to DAT_20003ce4 and write 1s back to them |
| [`hal_sys_timer_alarm_elapsed`](#hal_sys_timer_alarm_elapsed) | 0x0C0330FC | Ticks elapsed on the free-running counter since the alarm was armed |
| [`hal_sys_timer_alarm_get_count`](#hal_sys_timer_alarm_get_count) | 0x0C0330F0 | Read the alarm timer current-value register |
| [`hal_sys_timer_alarm_is_running`](#hal_sys_timer_alarm_is_running) | 0x0C0330E0 | Return whether the alarm timer enable bit is set |
| [`hal_sys_timer_alarm_start`](#hal_sys_timer_alarm_start) | 0x0C03308C | Arm the 0x4000200x timer for a one-shot wake after param_1 ticks |
| [`hal_sys_timer_alarm_stop`](#hal_sys_timer_alarm_stop) | 0x0C0330B8 | Stop the alarm timer and clear its pending interrupt |
| [`hal_sys_timer_calc_loop_ticks`](#hal_sys_timer_calc_loop_ticks) | 0x0C086754 | Measure timer ticks taken by a busy loop of N iterations, optionally the DWT cycle cost of a timer read |
| [`hal_sys_timer_delay_us`](#hal_sys_timer_delay_us) | 0x0C033030 | Busy-wait for param_1 microseconds on the hardware tick counter |
| [`hal_sysipc_close`](#hal_sysipc_close) | 0x0C03171C | Release one user of an IPC channel and shut the channel down when unused |
| [`hal_sysipc_rx_irq_disable`](#hal_sysipc_rx_irq_disable) | 0x0C031848 | Disable the NVIC interrupt of an IPC channel |
| [`hal_sysipc_rx_irq_setup`](#hal_sysipc_rx_irq_setup) | 0x0C031978 | Enable the IPC channel interrupt and (channel 1) install its vector and priority |
| [`hal_sysipc_send`](#hal_sysipc_send) | 0x0C031884 | Queue a two-word IPC message on channel 0/1 for user type 0/1 and ring the doorbell (0x400000a0) |
| [`hal_trace_buf_putc`](#hal_trace_buf_putc) | 0x0C035684 | Append a byte to a line buffer and flush through a write callback when full |
| [`hal_trace_get_state_vars`](#hal_trace_get_state_vars) | 0x0C0363A4 | Copy three global words (0x2000baac, baa8, baa4) to caller-provided pointers |
| [`hal_trace_set_flag_baa4`](#hal_trace_set_flag_baa4) | 0x0C036388 | Set the global flag at 0x2000baa4 to 1 |
| [`hwtimer_handler`](#hwtimer_handler) | 0x0C041ED4 | Sys-timer alarm ISR of the hwtimer list: expire due timers, re-arm the alarm and run callbacks |
| [`hwtimer_start`](#hwtimer_start) | 0x0C042170 | Validate a hwtimer id against the static pool and start it with the given tick timeout |
| [`hwtimer_start_internal`](#hwtimer_start_internal) | 0x0C04200C | Insert a hwtimer into the delta-sorted active list and (re)arm the sys-timer alarm (BES __hwtimer_start) |
| [`hwtimer_stop`](#hwtimer_stop) | 0x0C04219C | Remove a hwtimer from the active or expired list, fixing deltas and re-arming the alarm |
| [`norflaship_cfg38_clear_bit12`](#norflaship_cfg38_clear_bit12) | 0x0C0879C0 | Clear bit 12 of register REG_038 |
| [`norflaship_cfg38_set_bit0`](#norflaship_cfg38_set_bit0) | 0x0C0879D4 | Set bit 0 of register REG_038 |
| [`norflaship_cfg38_set_bit12`](#norflaship_cfg38_set_bit12) | 0x0C0879AC | Set bit 12 of register REG_038 |
| [`norflaship_clear_fifos`](#norflaship_clear_fifos) | 0x0C0877E4 | Reset both TX and RX FIFOs of the flash IP |
| [`norflaship_clear_rxfifo`](#norflaship_clear_rxfifo) | 0x0C087800 | Reset the RX FIFO of the flash IP |
| [`norflaship_clear_txfifo`](#norflaship_clear_txfifo) | 0x0C08781C | Reset the TX FIFO of the flash IP |
| [`norflaship_ctrl_clear_bit0`](#norflaship_ctrl_clear_bit0) | 0x0C087774 | Wait for idle, then clear bit 0 of REG_004 |
| [`norflaship_ctrl_clear_bit25`](#norflaship_ctrl_clear_bit25) | 0x0C0875C8 | Clear bit 25 of flash-IP control register REG_004 after waiting for idle |
| [`norflaship_ctrl_set_bit25`](#norflaship_ctrl_set_bit25) | 0x0C0875E4 | Set bit 25 of flash-IP control register REG_004 after waiting for idle |
| [`norflaship_fill_txfifo`](#norflaship_fill_txfifo) | 0x0C08765C | Push up to FIFO-space bytes from a buffer into the TX FIFO |
| [`norflaship_get_cfg14_byte2`](#norflaship_get_cfg14_byte2) | 0x0C08785C | Read bits 16..23 of config register REG_014 |
| [`norflaship_read_rxfifo_byte`](#norflaship_read_rxfifo_byte) | 0x0C0876A0 | Read the low byte of flash-IP register REG_010 (RX data) |
| [`norflaship_send_cmd_byte`](#norflaship_send_cmd_byte) | 0x0C0876D4 | Issue a command opcode with one operand byte (REG_004 bit0 cleared) |
| [`norflaship_send_cmd_ext`](#norflaship_send_cmd_ext) | 0x0C08772C | Start a transaction with command, data length and extended field |
| [`norflaship_send_cmd_word`](#norflaship_send_cmd_word) | 0x0C0876F4 | Start a transaction with a raw command word and length (REG_004 bit0 set) |
| [`norflaship_set_cfg14_bit3`](#norflaship_set_cfg14_bit3) | 0x0C0878D8 | Set or clear bit 3 of config register REG_014 (no idle wait) |
| [`norflaship_set_cfg14_bit4`](#norflaship_set_cfg14_bit4) | 0x0C0878B4 | Set or clear bit 4 of config register REG_014 after waiting for idle |
| [`norflaship_set_cfg14_bit5`](#norflaship_set_cfg14_bit5) | 0x0C087890 | Set or clear bit 5 of config register REG_014 after waiting for idle |
| [`norflaship_set_cfg14_byte2`](#norflaship_set_cfg14_byte2) | 0x0C087838 | Set bits 16..23 of config register REG_014 after waiting for idle |
| [`norflaship_set_cfg14_nibble3`](#norflaship_set_cfg14_nibble3) | 0x0C087870 | Set bits 12..15 of config register REG_014 after waiting for idle |
| [`norflaship_set_cfg38_width_sel`](#norflaship_set_cfg38_width_sel) | 0x0C087978 | Map a size/width value to the 2-bit selector REG_038[14:13] |
| [`norflaship_set_ctrl_field_4_11`](#norflaship_set_ctrl_field_4_11) | 0x0C0875A8 | Set bits 4..11 of flash-IP control register REG_004 after waiting for idle |
| [`norflaship_set_len_and_fill_txfifo`](#norflaship_set_len_and_fill_txfifo) | 0x0C087600 | Program transfer length and push bytes into the TX FIFO |
| [`norflaship_set_reg108`](#norflaship_set_reg108) | 0x0C087A0C | Write a 5-bit value to register REG_108 |
| [`norflaship_set_reg20_byte0`](#norflaship_set_reg20_byte0) | 0x0C087944 | Set bits 0..7 of register REG_020 |
| [`norflaship_set_reg20_byte2`](#norflaship_set_reg20_byte2) | 0x0C087928 | Set bits 16..23 of register REG_020 |
| [`norflaship_set_reg30_top_byte`](#norflaship_set_reg30_top_byte) | 0x0C0878F8 | Write the top byte of a word to register REG_030 |
| [`norflaship_set_reg40_bits2_3`](#norflaship_set_reg40_bits2_3) | 0x0C0879E8 | Set or clear bits 2..3 (mask 0xC) of register REG_040 |
| [`norflaship_set_xfer_len`](#norflaship_set_xfer_len) | 0x0C0876B0 | Set transfer length field REG_004[24:12] of the flash IP |
| [`norflaship_wait_fifo_level`](#norflaship_wait_fifo_level) | 0x0C087790 | Busy-wait until REG_00C[7:4] reaches a minimum level |
| [`norflaship_wait_idle`](#norflaship_wait_idle) | 0x0C0877BC | Busy-wait until the flash controller is no longer busy |
| [`nvic_clear_pending_irq`](#nvic_clear_pending_irq) | 0x0C03AA9C | Clear the NVIC pending bit of an external interrupt |
| [`nvic_disable_irq`](#nvic_disable_irq) | 0x0C03AAE0 | Disable an external interrupt in the NVIC |
| [`nvic_set_default_priority_and_enable_irq`](#nvic_set_default_priority_and_enable_irq) | 0x0C03AAB8 | Set IRQ priority to 0x60 and enable it in the NVIC |
| [`pm_busy_mask_clear_bit`](#pm_busy_mask_clear_bit) | 0x0C031C90 | Clear bit n in the global bitmask DAT_2000aa6c (n < 32) |
| [`pm_busy_mask_set_bit`](#pm_busy_mask_set_bit) | 0x0C031C40 | Set bit n in the global bitmask DAT_2000aa6c (n < 32) |
| [`pm_wake_mask_clear_bit`](#pm_wake_mask_clear_bit) | 0x0C031D2C | Clear bit n in the global bitmask DAT_2000aa68 (n < 32) |
| [`pm_wake_mask_set_bit`](#pm_wake_mask_set_bit) | 0x0C031CDC | Set bit n in the global bitmask DAT_2000aa68 (n < 32) |
| [`systick_measure_loop_us`](#systick_measure_loop_us) | 0x0C03F7CC | Time a busy loop of param_1 iterations with SysTick and return the duration in microseconds (or -1 on wrap) |
| [`thunk_bes_gpio_read_status_words`](#thunk_bes_gpio_read_status_words) | 0x0C041B5C | Tail-branch thunk to bes_gpio_read_status_words (0x0c041ab0) |

## analogif_reg3037_3048_config

**Read-modify-write analog registers 0x3037 (clear bits 7-8) and 0x3048 (set bit 13)**

Uses the analog register read thunk FUN_0c089468 (-> 0x0c040290) and write thunk FUN_0c0894a8 (-> 0x0c0401b0): reads 0x3037, masks with 0xFE7F (clears bits 7 and 8) and writes it back; reads 0x3048, ORs 0x2000 (bit 13) and writes it back. The decompiler drops the value argument of the writes but the modified local is passed in r1. A static configuration step of the same 0x30xx analog interface used by ble_219_0c086b04; no direct callers.

- Addresses by version: 219: 0x0C086C30
- Calls: `ble_thunk_call_0c0401b0`, `ble_thunk_call_0c040290`
- Confidence: low

## analogif_reg30b7_channel_read

**Sequence writes to analog register 0x30B7 to sample channel N and read the result from 0x30BE|0x30BD**

Drives an analog/PMU style register interface through the thunks FUN_0c0894a8 (write reg,val -> 0x0c0401b0) and FUN_0c089468 (read reg,&val -> 0x0c040290). Sequence on register 0x30B7: write 8, write 0x18, write (param_1<<6)|0x18, write (param_1<<6)|0x38 (if that write fails the final pair becomes 0x28/0x20), write (param_1<<6)|0x18 again, then read registers 0x30BE and 0x30BD and OR the two 16-bit values into *param_2 (result split over two registers). Every path ends by writing 0x30B7 = 8 (or 0x28) and then 0 (or 0x20), returning the interface to its idle setting. Each write's return value is checked and the sequence aborts to the cleanup on the first failure. Looks like a one-shot ADC/measurement trigger on channel param_1 (bits 6..); no direct callers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | channel/selector placed in bits 6.. of register 0x30B7 |
| `param_2` | `ptr` | u16 * receiving (reg 0x30BE \| reg 0x30BD) |

**Notes:** The register block 0x30xx is accessed only through the undescribed thunks; its identity (RF/PMU analog interface) and the meaning of the bit fields are guesses.

- Addresses by version: 219: 0x0C086B04
- Calls: `ble_thunk_call_0c0401b0`, `ble_thunk_call_0c040290`
- Confidence: low

## bes_analog_clock_mode_config

**Program analog/clock config registers 0xD0220C18 and 0xD0220C90 for mode 2, 3 or default**

Read-modify-write on two undocumented registers in the 0xD022xxxx block. mode 2: reg 0xC18 |= 0x2800000 and reg 0xC90 field [30:24] = 0x31. mode 3: reg 0xC90 field [30:24] = 0x5B and reg 0xC18 |= 0x2C00000. Any other value: reg 0xC18 |= 0x2000000 only. It looks like selection of a PLL/oscillator or RF clock configuration with different divider/trim values per mode. Called from the larger init routine 0x0c03c4bc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | mode selector: 2 or 3 select special settings, anything else is the default |

**Notes:** Block 0xD0220000 is not documented; interpretation as a clock/PLL setup is a guess based on the call context.

- Addresses by version: 219: 0x0C03C30C
- Called by: `bt_drv_rf_apply_config`
- Confidence: low

## bes_analog_init_defaults

**Initialise four registers in the 0xD0220C0C..0xD0220C8C analog block**

Performs read-modify-write on: 0xD0220C0C clear bits [15:11] and set bit 13; 0xD0220C80 clear bits [17:15], [11:9] and set bit 1; 0xD0220C18 clear bits 8 and 0; 0xD0220C8C clear bits [30:29]. Looks like a part of the analog/power block bring-up. Called from the init sequence 0x0c03cdfc.

**Notes:** Registers undocumented; the 'defaults' reading is inferred from the fact that it is called unconditionally from an init sequence.

- Addresses by version: 219: 0x0C03C7B0
- Called by: `bt_drv_rf_init`
- Confidence: low

## bes_analog_set_c10_field

**Enable (with a 4-bit value) or disable a field in register 0xD0220C10**

If param_1 != 0: reg 0xD0220C10 bits [28:25] = param_2 & 0xF and bit 29 is set. If param_1 == 0: bit 29 is cleared and the 4-bit field is left unchanged. Looks like an enable bit plus a 4-bit trim/gain value in the analog block. Called from 0x0c03c4bc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | non-zero to enable and program the field, 0 to disable |
| `param_2` | `u32` | 4-bit value (masked with 0xF) written to bits 28:25 |

**Notes:** Function of register 0xD0220C10 not known.

- Addresses by version: 219: 0x0C03C470
- Called by: `bt_drv_rf_apply_config`
- Confidence: low

## bes_aon_reg38_staged_release

**Write the 0xCAFE02xx key sequence FF->F7->F3->F1->F0 to 0x40085038 with delays**

Writes 0xCAFE02FF to register 0x40085038 (upper half 0xCAFE acts as a write key), waits one unit (thunk 0x0c073cb0(1) converts the value, thunk 0x0c073cc0 = hal_sys_timer_delay sleeps), writes 0xCAFE02F7 (bit 3 cleared), waits again, then writes 0xCAFE02F3, 0xCAFE02F1 and 0xCAFE02F0 back to back, clearing bits 2, 1 and 0 in turn. This is a staged release of four control bits (reset/isolation/power gates of a sub-block in the 0x40085000 AON peripheral) in a fixed order. Called from 0x0c03bb70.

**Notes:** 0x40085000 also hosts the AON GPIO status words (bes_gpio_read_status_words); what the four bits gate is unknown.

- Addresses by version: 219: 0x0C041A68
- Peripheral registers: `0x40085038` (W)
- Called by: `ble_219_0c03bb70`
- Calls: `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: low

## bes_calib_get_trim_pair

**Return two 16-bit calibration words: defaults, or OTP trims plus 12000 and 16200**

If DAT_2000BCD2 is zero it stores the defaults 0x32F0 (12528) to *param_1 and 0x4330 (17200) to *param_2. Otherwise it reads OTP fields 3 and 4 through RAM-patch thunk 0x2000067C (via 0x0C073C80) into the two outputs, keeps the low 11 bits of each, and adds 12000 (0x2EE0) and 16200 (0x3F48). The meaning of the two values (oscillator or RF calibration) is not established in this packet.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output: first 16-bit calibration word |
| `param_2` | `ptr` | output: second 16-bit calibration word |
| `param_3` | `u32` | passed to the OTP read |
| `param_4` | `u32` | passed to the OTP read |

- Addresses by version: 219: 0x0C03A1B0
- Called by: `hal_gpadc_adc2volt`
- Calls: `ble_ram_patch_thunk_2000067c`
- Confidence: medium

## bes_cmu_bit29_ctrl

**Write bit 29 to the 0x40000060 (param=0) or 0x40000064 (param!=0) register**

If param_1 == 0 writes 0x20000000 to 0x40000060, otherwise writes 0x20000000 to 0x40000064; returns 0. These two registers behave as a set/clear pair (see bes_cmu_set_sysclk_cfg), so this toggles one clock/power-control bit (bit 29). Called from ble_219_0c040cfc, together with the bit-30 variant at 0x0c040ce8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 0 = write to register 0x40000060, nonzero = write to 0x40000064 |

**Returns** `u32`: always 0

**Notes:** Which register enables and which disables is inferred.

- Addresses by version: 219: 0x0C040CD0
- Peripheral registers: `0x40000060` (W), `0x40000064` (W)
- Called by: `hal_cmu_sys_pll_restart`
- Confidence: medium

## bes_cmu_bit30_ctrl

**Write bit 30 to the 0x40000060 (param=0) or 0x40000064 (param!=0) register**

Same as bes_cmu_bit29_ctrl but for bit 30: param_1 == 0 writes 0x40000000 to 0x40000060, otherwise to 0x40000064; returns 0. Called from ble_219_0c040cfc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 0 = write to register 0x40000060, nonzero = write to 0x40000064 |

**Returns** `u32`: always 0

**Notes:** Which register enables and which disables is inferred.

- Addresses by version: 219: 0x0C040CE8
- Peripheral registers: `0x40000000` (A), `0x40000060` (W), `0x40000064` (W)
- Called by: `hal_cmu_sys_pll_restart`
- Confidence: medium

## bes_cmu_reg5c_clear_bit9

**Clear bit 9 of peripheral register 0x4000005c under BASEPRI lock**

Read-modify-write of 0x4000005c: value &= 0xfffffdff, i.e. clears bit 9. Part of the BES clock/power control block (0x40000000 base, address only, undocumented); the paired function at 0x0c040a20 sets bit 10 of the same register. Both are called from ble_219_0c032ee8. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored).

**Notes:** Exact meaning of bit 9 / bit 10 of 0x4000005c unknown (likely a clock or oscillator gate/select).

- Addresses by version: 219: 0x0C0409E4
- Peripheral registers: `0x4000005c` (RW)
- Called by: `bes_cmu_init_periph_pair`
- Confidence: medium

## bes_cmu_reg5c_set_bit10

**Set bit 10 of peripheral register 0x4000005c under BASEPRI lock**

Read-modify-write of 0x4000005c: value |= 0x400, i.e. sets bit 10. Counterpart of the function at 0x0c0409e4 (clears bit 9); both are called from ble_219_0c032ee8, probably as a pair that switches a clock/oscillator selection. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored).

**Notes:** Meaning of the bit is not documented.

- Addresses by version: 219: 0x0C040A20
- Peripheral registers: `0x4000005c` (RW)
- Called by: `bes_cmu_init_periph_pair`
- Confidence: medium

## bes_cmu_set_reg70_sel_b12

**Clear or set a selector field in 0x40000070 (0 = clear, 1 = set), under BASEPRI lock**

Raises BASEPRI to 0x40, then if param_1 == 0 clears bits 14..12 (mask 0x7000) of 0x40000070 (read-modify-write); if param_1 == 1 clears the field and sets bit 12 (0x1000); any other value leaves the register untouched and returns 1. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored). Looks like a binary clock-source / divider selector in the BES clock-management block, but the register is undocumented.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 0 = clear field, 1 = set field, other = invalid |

**Returns** `u32`: 0 on success, 1 if param_1 is not 0 or 1

- Addresses by version: 219: 0x0C040E08
- Peripheral registers: `0x40000070` (RW)
- Called by: `hal_uart_set_baud_divisor`
- Confidence: medium

## bes_cmu_set_reg70_sel_b2

**Clear or set a selector field in 0x40000070 (0 = clear, 1 = set), under BASEPRI lock**

Raises BASEPRI to 0x40, then if param_1 == 0 clears bits 4..2 (mask 0x1c) of 0x40000070 (read-modify-write); if param_1 == 1 clears the field and sets bit 2 (0x4); any other value leaves the register untouched and returns 1. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored). Looks like a binary clock-source / divider selector in the BES clock-management block, but the register is undocumented.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 0 = clear field, 1 = set field, other = invalid |

**Returns** `u32`: 0 on success, 1 if param_1 is not 0 or 1

- Addresses by version: 219: 0x0C040D58
- Peripheral registers: `0x40000070` (RW)
- Called by: `hal_uart_set_baud_divisor`
- Confidence: medium

## bes_cmu_set_reg70_sel_b7

**Clear or set a selector field in 0x40000070 (0 = clear, 1 = set), under BASEPRI lock**

Raises BASEPRI to 0x40, then if param_1 == 0 clears bits 9..7 (mask 0x380) of 0x40000070 (read-modify-write); if param_1 == 1 clears the field and sets bit 7 (0x80); any other value leaves the register untouched and returns 1. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored). Looks like a binary clock-source / divider selector in the BES clock-management block, but the register is undocumented.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 0 = clear field, 1 = set field, other = invalid |

**Returns** `u32`: 0 on success, 1 if param_1 is not 0 or 1

- Addresses by version: 219: 0x0C040DB0
- Peripheral registers: `0x40000070` (RW)
- Called by: `hal_uart_set_baud_divisor`
- Confidence: medium

## bes_cmu_set_reg74_sel_b3

**Clear or set a selector field in 0x40000074 (0 = clear, 1 = set), under BASEPRI lock**

If param_1 == 0 clears bits 5..3 of 0x40000074; if 1 clears them and sets bit 3 (0x8); otherwise returns 1 without touching the register. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored). Binary selector in the BES clock block; called from ble_219_0c0458a6.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 0 or 1 |

**Returns** `u32`: 0 on success, 1 for invalid param

- Addresses by version: 219: 0x0C040EC0
- Peripheral registers: `0x40000074` (RW)
- Called by: `ble_219_0c0458a6`
- Confidence: medium

## bes_cmu_set_rega8_bit21

**Clear (0) or set (1) bit 21 of 0x400000a8 under BASEPRI lock**

If param_1 == 0 clears bit 21 (0x200000) of 0x400000a8; if 1 sets it; otherwise returns 1. The low 2 bits of the same register are used by bes_cmu_set_sysclk_cfg. Called from ble_219_0c031da0 and the hardware init routine ble_219_0c03ab80. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 0 = clear, 1 = set |

**Returns** `u32`: 0 on success, 1 for invalid param

- Addresses by version: 219: 0x0C040F18
- Peripheral registers: `0x400000a8` (RW)
- Called by: `hal_spi_apply_cfg_regs`, `ble_219_0c03ab80`
- Confidence: medium

## bes_cmu_set_sysclk_cfg

**Apply clock-gate enable/disable masks for a system-clock configuration index 0..7**

Returns 1 for param_1 > 7. For 0..6 loads three words from tables at 0x0c0745a8 (mask written to 0x40000060), 0x0c0745c4 (mask written to 0x40000064) and 0x0c0745e0 (2-bit selector, 0xffffffff = none). For 7 it uses built-in masks 0x1b00/0x20 and writes 0x20 then 0x1000 to 0x40000060 first. The byte DAT_20003d87 (see bes_cmu_set_sysclk_mode) alters the masks (bits 0x20 and 0x1000 are cleared/swapped; mode >=2 supplies the selector as mode-2). If a selector is present, the low 2 bits of 0x400000a8 are replaced under a BASEPRI lock. Finally the set mask goes to 0x40000060 and the clear mask to 0x40000064 in an order that first asserts 0x20 / 0x1000 and then removes 0x1000/0x20, i.e. a glitch-free clock switch. Called from the BES hal init (ble_219_0c03ab80) and ble_219_0c032c04/0c039820/0c0399b4. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | configuration index 0..7 |

**Returns** `u32`: 0 on success, 1 if index > 7

**Notes:** 0x40000060 is assumed to be the set/enable register and 0x40000064 the clear/disable register of a pair; bit meanings (0x20, 0x800, 0x1000, 0x200..) are inferred, tables not decoded.

- Addresses by version: 219: 0x0C040BC8
- Peripheral registers: `0x40000060` (W), `0x40000064` (W), `0x400000a8` (RW)
- Called by: `bes_cmu_request_sysclk`, `ble_219_0c039820`, `ble_219_0c0399b4`, `ble_219_0c03ab80`
- Confidence: medium

## bes_cmu_set_sysclk_mode

**Store the clock-switch mode byte used by bes_cmu_set_sysclk_cfg**

Stores param_1 into the byte DAT_20003d87. bes_cmu_set_sysclk_cfg (0x0c040bc8) reads it: 0 selects the default sequence, 1 and >=2 select alternative enable/disable mask combinations (and, for >=2, a value written to the low 2 bits of 0x400000a8). Called from ble_219_0c0399b4, which also calls the config function.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | mode: 0 = default, 1 = alt A, >=2 = alt B (value-2 goes to 0x400000a8[1:0]) |

**Notes:** Name of the mode is inferred from its single consumer.

- Addresses by version: 219: 0x0C040BBC
- Called by: `ble_219_0c0399b4`
- Confidence: medium

## bes_cmu_stub_return_0

**Stub that returns 0**

Empty hook that just returns 0 (status OK). It is called once from the hardware init routine ble_219_0c03ab80 and is a placeholder for an unused/disabled platform step.

**Returns** `u32`: always 0

- Addresses by version: 219: 0x0C040CCC
- Called by: `ble_219_0c03ab80`
- Confidence: high

## bes_gpio_mask_clear

**Clear bit for pin 0..35 in the mask words 0x40085080 (0-31) / 0x40085084 (32-35)**

Inverse of bes_gpio_mask_set: clears bit param_1 in 0x40085080 for pins < 0x20, or bit param_1-0x20 in 0x40085084 for pins 0x20..0x23. Called from ble_219_0c0300d0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | pin index 0..35 |

**Notes:** Role as a per-pin interrupt/wake mask is inferred.

- Addresses by version: 219: 0x0C041B20
- Peripheral registers: `0x40085080` (RW), `0x40085084` (RW)
- Called by: `ble_219_0c0300d0`
- Confidence: medium

## bes_gpio_mask_set

**Set bit for pin 0..35 in the mask words 0x40085080 (0-31) / 0x40085084 (32-35)**

If param_1 < 0x20 sets bit param_1 in 0x40085080, else if param_1 < 0x24 sets bit (param_1-0x20) in 0x40085084; larger values are ignored. Called from ble_219_0c0300d0. Not interrupt-protected.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | pin index 0..35 |

**Notes:** Role as a per-pin interrupt/wake mask is inferred.

- Addresses by version: 219: 0x0C041AE8
- Peripheral registers: `0x40085080` (RW), `0x40085084` (RW)
- Called by: `ble_219_0c0300d0`
- Confidence: medium

## bes_gpio_read_status_words

**Copy up to three 32-bit status words from 0x4008508c/90/94 into a buffer**

Reads 0x4008508c into out[0] if param_2 >= 1, 0x40085090 into out[1] if param_2 >= 2, and (0x40085094 & 0xffff) into out[2] if param_2 >= 3. Returns the number of words handled, min(param_2, 3) (0 when param_2 is 0). Called from ble_219_0c041b5c. These status words correspond to the 36-pin mask group at 0x40085080/84 (pins 0..35).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output array of u32 (3 entries) |
| `param_2` | `u32` | number of words requested |

**Returns** `u32`: words written, 0..3

**Notes:** Interpretation as pin interrupt/wake status is inferred.

- Addresses by version: 219: 0x0C041AB0
- Peripheral registers: `0x4008508c` (R), `0x40085090` (R), `0x40085094` (R)
- Called by: `thunk_bes_gpio_read_status_words`
- Confidence: medium

## bes_hw_get_const_4000

**Return the constant 4000**

Returns 4000. Used by two callers (ble_219_0c03ac44 and ble_219_0c03cd58), likely a platform parameter such as a timing/wake-up margin in us or ticks.

**Returns** `u32`: constant 4000

**Notes:** Unit and purpose of the constant are unknown.

- Addresses by version: 219: 0x0C041328
- Called by: `ble_219_0c03ac44`, `ble_219_0c03cd58`
- Confidence: low

## bes_hw_init_clock_power_regs

**Write the default configuration of the clock/power and system register blocks at boot**

Long straight-line init: sets bits in 0x4008004c, programs 0x40080008/0x40080010/0x40080044/0x40080048/0x4008001c/0x40080068, loads 0x400000d4..0x400000e8 with constant words (0x040c2040, 0x09207185, 0x1234c2f4, 0x185d6554, 0x1d734d19, 0x228607de) with the low 6-bit fields of 0x40000068/0x400000ec set to 0x13/0x23, writes 0xff to 0x40000150/0x40000144 and writes the same mask patterns (0x020ff794, 0x001ffdf2, 0x10dfa000, 0x00100000, 8, 0x80000000) to the register pairs 0x40000004/0c/14 and 0x40000034/3c/44 (looks like bulk clock-gate disable/enable of HCLK/PCLK/OCLK domains), clears fields in 0x4000001c, 0x4008006c, 0x40080084, 0x400800d0, sets bit 15 of 0x4008b0fc and zeroes the 0x40085000 block (0x40085080/84/98/9c/b0/b4 = 0, 0x40085088 = 0x12f0000, 0x400850a0 = 0x400000, 0x400850b8 = 0x900000, 0x40085008 = 0, 0x4008500c = 0x100). Called once from the chip init routine ble_219_0c03ab80.

**Notes:** Individual register/bit meanings are undocumented; the description is of the observed writes only.

- Addresses by version: 219: 0x0C04110C
- Peripheral registers: `0x40000004` (W), `0x4000000c` (W), `0x40000014` (W), `0x4000001c` (RW), `0x40000034` (W), `0x4000003c` (W), `0x40000044` (W), `0x40000068` (RW), `0x400000d4` (W), `0x400000d8` (W), `0x400000dc` (W), `0x400000e0` (W), `0x400000e4` (W), `0x400000e8` (W), `0x400000ec` (RW), `0x40000144` (W)
- Called by: `ble_219_0c03ab80`
- Confidence: medium

## bes_hw_nop_hook

**Empty hook function (bx lr)**

Does nothing and returns immediately. Called from the hardware init routine ble_219_0c03ab80 as a placeholder for an unused platform step.

- Addresses by version: 219: 0x0C0410E4
- Called by: `ble_219_0c03ab80`
- Confidence: high

## bes_iomux_apply_default_pin_cfg

**For all 36 pins whose function nibble is 0xf, clear a bit in one register and set it in another**

Writes 0xffffffff to 0x40086008 and 0 to 0x400860c4, then loops over pins 0..35. The 4-bit function field of pin n is read from 0x40086004 + (n>>3)*4 (pins 0-31) or 0x4008607c (pins 32-35), nibble (n&7). If the nibble equals 0xf (unassigned), bit n is cleared in 0x4008602c (pins 0-31) / 0x40086094 (32-35) and set in 0x40086030 / 0x40086098. Called from the init routine ble_219_0c03ab80. Looks like the IOMUX (base 0x40086000) default setup that disables pull/drive for unused pins.

**Notes:** Exact meaning of the registers 0x4008602c/0x40086030 (pull-up/enable pair?) is a guess.

- Addresses by version: 219: 0x0C041638
- Peripheral registers: `0x40086004` (R), `0x40086008` (W), `0x4008602c` (RW), `0x40086030` (RW), `0x4008607c` (R), `0x40086094` (RW), `0x40086098` (ARW), `0x400860c4` (W)
- Called by: `ble_219_0c03ab80`
- Confidence: medium

## bes_iomux_get_pin_table_entry

**Look up a byte in the 36x6 pin table at 0x0c08355c**

Returns table[param_2 + param_1*6] from a flash byte table at 0x0c08355c if param_1 < 0x24 (pin number) and param_2 < 6, else 0. Called from ble_219_0c0456c0. The table is probably a per-pin function/mux code map.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | pin index 0..35 |
| `param_2` | `u32` | column 0..5 |

**Returns** `u8`: table byte, or 0 when out of range

**Notes:** Table contents not decoded; purpose inferred.

- Addresses by version: 219: 0x0C041A00
- Called by: `ble_219_0c0456c0`
- Confidence: medium

## bes_iomux_init_level2

**Program the 0x40086000 block to level 2 and then clear bits 19:18 of 0x4008602c and 0x40086030**

Calls bes_iomux_reg0c_set_level(2) (0x0c0414e0), then inside its own BASEPRI 0x40 critical section (lock-owner trace in DAT_20003D70/74) waits for the RAM thunk 0x0c073c40(0) to return non-zero, clears bits 19:18 of both 0x4008602c and 0x40086030 and calls the RAM thunk 0x0c073ba0(0) (commit). Part of the CMU/board setup performed by 0x0c03ab80, its only caller.

**Notes:** Register meaning unknown; grouped with bes_iomux_reg0c_set_level and the bes_iomux_reg44_* helpers.

- Addresses by version: 219: 0x0C041884
- Peripheral registers: `0x40086000` (A), `0x4008602c` (RW), `0x40086030` (RW)
- Called by: `ble_219_0c03ab80`
- Calls: `bes_iomux_reg0c_set_level`, `ble_ram_patch_thunk_2000025c`, `ble_ram_patch_thunk_20000244`
- Confidence: low

## bes_iomux_reg0c_set_level

**Under lock, wait for the 0x40086000 block to be idle and program nibbles 11:8 and 15:12 of 0x4008600c to param_1**

Enters a BASEPRI 0x40 critical section with the DAT_20003D70/74 lock-owner trace, then spins until the RAM thunk 0x0c073c40 (0x20000244) returns non-zero with argument 0 (a ready/idle poll). It then sets bits 1:0 of 0x40086050, rewrites 0x4008600c so that bits 11:8 and 15:12 both hold param_1 (mask 0xFFFF00FF), sets bit 18 of 0x4008602c and then clears bit 19 of it (two separate read-modify-writes), clears bits 19:18 of 0x40086030 and calls the RAM thunk 0x0c073ba0 (0x2000025C) with 0, before restoring BASEPRI. Called with 2 from bes_iomux_init_level2 (0x0c041884) and from 0x0c0456c0. The 0x40086000 block is the one accessed by bes_iomux_reg44_set_bits/clear_bits.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 4-bit level/selector value written to both nibbles 11:8 and 15:12 of 0x4008600c |

**Notes:** Register semantics unknown (BES-specific); the thunk pair 0x0c073c40/0x0c073ba0 looks like a bus-idle wait and a commit/flush.

- Addresses by version: 219: 0x0C0414E0
- Peripheral registers: `0x40086000` (A), `0x4008600c` (RW), `0x4008602c` (RW), `0x40086030` (RW), `0x40086050` (RW)
- Called by: `bes_iomux_init_level2`, `ble_219_0c0456c0`
- Calls: `ble_ram_patch_thunk_2000025c`, `ble_ram_patch_thunk_20000244`
- Confidence: low

## bes_iomux_reg44_clear_bits

**Clear bits in 0x40086044 and return the previous low 16 bits**

Reads 0x40086044 (old), reads it again, writes (value & ~param_1) and returns old & 0xffff. Called from ble_219_0c040290.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bitmask to clear |

**Returns** `u32`: previous value of 0x40086044 bits 15..0

- Addresses by version: 219: 0x0C0418F4
- Peripheral registers: `0x40086044` (RW)
- Called by: `hal_analogif_reg_write`
- Confidence: medium

## bes_iomux_reg44_set_bits

**Set bits in 0x40086044 and return the previous low 16 bits**

Reads 0x40086044 (old), reads it again, writes (value | param_1) and returns old & 0xffff. Called from ble_219_0c040290 together with bes_iomux_reg44_clear_bits.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bitmask to set |

**Returns** `u32`: previous value of 0x40086044 bits 15..0

- Addresses by version: 219: 0x0C0418E0
- Peripheral registers: `0x40086044` (RW)
- Called by: `hal_analogif_reg_write`
- Confidence: medium

## bes_otp_load_variant

**Load a 2-bit hardware variant from OTP word 0xC into DAT_20003D64**

If bes_sysreg_read_80000_hi16 (0x0C0413E4) returns zero and the sticky flag DAT_20003D65 is clear, it reads OTP field 0xC through RAM-patch thunk 0x2000067C into a 16-bit local. It then stores bits 7..8 in DAT_20003D64 when that 2-bit value is 0, 1 or 2; the value 3 leaves the variable unchanged. Otherwise it sets DAT_20003D65 (when the sysreg value is nonzero) and forces DAT_20003D64 to 3. The meaning of the variant is not identified in this packet.

- Addresses by version: 219: 0x0C0385FC
- Called by: `ble_219_0c038d68`
- Calls: `bes_sysreg_read_80000_hi16`, `ble_ram_patch_thunk_2000067c`
- Confidence: medium

## bes_pack_two_14bit_fields

**Pack two 14-bit values into a 32-bit register image and clear bit 31 of 0xD0350250**

Clears bit 31 of the hardware register 0xD0350250, then writes *param_1 bits [13:0] = param_2 & 0x3FFF and bits [29:16] = param_3 & 0x3FFF (leaving the other bits). The two writes to *param_1 are separate read-modify-writes, so param_1 is probably a memory-mapped register. Called from 0x0c03f1f4.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | pointer to the 32-bit register or word receiving the two fields |
| `param_2` | `u32` | low field value (14 bits) |
| `param_3` | `u32` | high field value (14 bits) |

**Notes:** Which peripheral (possibly a DMA or timer count/limit pair) is not known.

- Addresses by version: 219: 0x0C03EF58
- Called by: `ble_219_0c03f1f4`
- Confidence: low

## bes_periph_d033_config

**Clear bit 7 of 0xD0330038 and set bit 18 / clear bit 5 of 0xD0330024**

Small read-modify-write on two registers in the 0xD033xxxx block: reg 0x38 bit 7 is cleared; reg 0x24 bit 5 is cleared and bit 18 is set. Called from 0x0c03bb70 (hardware bring-up). Purpose of the bits is unknown.

**Notes:** Undocumented block 0xD0330000.

- Addresses by version: 219: 0x0C03CD38
- Called by: `ble_219_0c03bb70`
- Confidence: low

## bes_periph_d035_init_main

**Big one-shot initialisation of the 0xD0350xxx register block, including two RAM buffer pointers**

Writes about 40 registers in the 0xD03500xx..0xD03503xx block: read-modify-write of fields (0xD0350214, 324, 210, 254, 0D0, 240, 300, 308, 340, 344, 370, 014) and direct writes of constants (0xD0350010=0x37100032, 004=0x02910055, 36C=0x04801000, 040=0x810115, 05C=0x014E1010, 120=0x00C80032, 2C0=0x00100087, 0E0=0x01FFFC85, 138=0x0FFF0FFF, 13C=0xFFF, 20C=0x1E011E1E, 018=2, 0D8=1). It also programs address registers 0xD03500E4..0xD0350100 with the RAM regions at 0x20000060 and 0x20004000 in several alias forms (0x10000060, 0x10004000, 0x08000060, 0x08004000, 0x80004000 ...) and two values 0x168174 / 0x5DC0C0 (about 6.144 MHz) into 0xD0350104/108. This looks like setup of a DMA/bus-master or audio/PCM-like peripheral with two buffers in SRAM, but the exact block is undocumented. Called from the init sequence 0x0c03cdfc.

**Notes:** Peripheral identity unknown; 0x5DC0C0 ~ 6.144 MHz suggests a clock-rate constant, and 0x20000060/0x20004000 are buffers.

- Addresses by version: 219: 0x0C03CA04
- Called by: `bt_drv_rf_init`
- Confidence: low

## bes_periph_d035_init_small

**Initialise six registers in the 0xD0350240..0xD035035C block**

Read-modify-write on undocumented registers: 0xD035035C bits[1:0] = 1; 0xD0350240 set bit 12; low byte of 0xD035034C = 0x40; low byte of 0xD0350350 = 0x40; low byte of 0xD0350354 = 0x80; low nibble of 0xD0350358 = 6. Called from 0x0c03c930, which is part of the same hardware bring-up family as the large 0xD0350xxx init at 0x0c03ca04.

**Notes:** Block purpose unknown (clock/RF/analog bring-up?).

- Addresses by version: 219: 0x0C03C87C
- Called by: `bt_drv_rf_pre_init`
- Confidence: low

## bes_rf_set_mode_bits

**Set the 2-bit field at bits 13..14 of RF register 0xD0220C7C, bracketed by sysreg gates**

Thunk for ble_219_0c03e034, which is not described in this packet. When DAT_2000BD58 is zero it calls bes_sysreg_write_04_bit19 (0x0C0413F0) first. It then replaces bits 13..14 of the word at 0xD0220C7C with param_1 << 13 and, if the flag is still zero, calls bes_sysreg_write_08_bit19 (0x0C041430). The register block is identified only by its address.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | 2-bit field value 0..3 |

- Addresses by version: 219: 0x0C03BE88
- Called by: `ble_219_0c03e314`
- Calls: `bt_drv_rf_set_reg_c7c_bits13_14`
- Confidence: low

## bes_rf_synth_config_by_mode

**Set fields in 0xD0350xxx registers for mode 0 or 1; hangs on any other value**

Sets byte [15:8] of reg 0xD035020C to 0x1E and of 0xD0350210 to 0x20. For param_1 == 0 it sets bits [30:29] of 0xD0350228 and writes field [26:15] of 0xD0350048 = 0x44B; for param_1 == 1 it clears bits [30:29] of 0xD0350228 and writes field [26:15] of 0xD0350048 = 0x1064. Any other value falls into an endless loop (assert-style trap). Called from the init routine 0x0c03c4bc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | mode: 0 or 1 (anything else hangs the CPU) |

**Notes:** The 0xD035xxxx block is undocumented; it may be an RF/analog or clock synthesiser block. Two modes might be two crystal/clock frequencies.

- Addresses by version: 219: 0x0C03C380
- Called by: `bt_drv_rf_apply_config`
- Confidence: low

## bes_sysreg_ack_pending_bit8

**Write 0x4000000 to 0x40080040 and 0x100 to 0x40080004, with read-backs of 0x40080000**

Writes 0x04000000 to 0x40080040, reads 0x40080000 (read-back to flush the write), writes 0x100 to 0x40080004 and reads 0x40080000 again. Part of a three-step hardware sequence (with the functions at 0x0c041348 and 0x0c0413c4) all called from ble_219_0c03bb70, possibly sleep/wake configuration.

**Notes:** Bit meanings unknown; role as 'ack' is a guess.

- Addresses by version: 219: 0x0C041330
- Peripheral registers: `0x40080000` (R), `0x40080004` (W), `0x40080040` (W)
- Called by: `ble_219_0c03bb70`
- Confidence: low

## bes_sysreg_cfg_step2

**Reconfigure fields of 0x40080090/0x400800b0/0x4008003c then trigger via 0x40080014 and 0x400800cc**

Under a BASEPRI lock: 0x40080090 = (v & 0xc7fffc7f) | 0x380, 0x400800b0 = (v & 0xffff83e0) | 0x1f, 0x4008003c &= 0x00fffffe. After the lock: writes 0x4000000 to 0x40080014, reads 0x40080000, writes 0x48 to 0x400800cc and reads 0x40080000 again. Called from ble_219_0c03bb70 after the function at 0x0c041330. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored).

**Notes:** Purpose (likely power/sleep related) is not determinable from the code alone.

- Addresses by version: 219: 0x0C041348
- Peripheral registers: `0x40080000` (R), `0x40080014` (W), `0x4008003c` (RW), `0x40080090` (RW), `0x400800b0` (RW), `0x400800cc` (W)
- Called by: `ble_219_0c03bb70`
- Confidence: low

## bes_sysreg_cfg_step3

**Set field 0x82 in bits 15..8 of 0x4008006c and set bit 27 of 0x40080084**

0x4008006c = (v & 0xffff00ff) | 0x8200 and 0x40080084 |= 0x08000000. Third step of the sequence called from ble_219_0c03bb70.

**Notes:** Register meanings unknown.

- Addresses by version: 219: 0x0C0413C4
- Peripheral registers: `0x4008006c` (RW), `0x40080084` (RW)
- Called by: `ble_219_0c03bb70`
- Confidence: low

## bes_sysreg_read_80000_hi16

**Return the upper 16 bits of peripheral register 0x40080000**

Reads 0x40080000 and returns value >> 16. Called from ble_219_0c0385fc and ble_219_0c038d68. The same register is dummy-read elsewhere to flush posted writes, so it is a status/counter word in the system block.

**Returns** `u32`: bits 31..16 of 0x40080000

**Notes:** Field meaning unknown.

- Addresses by version: 219: 0x0C0413E4
- Peripheral registers: `0x40080000` (R)
- Called by: `bes_otp_load_variant`, `ble_219_0c038d68`
- Confidence: medium

## bes_sysreg_select_mode1

**Set the low 3-bit field of 0x4008005c and 0x400800b4 to 1**

Two read-modify-writes: 0x4008005c = (v & ~7) | 1 and 0x400800b4 = (v & ~7) | 1. Selects the same 3-bit mode value (1) in two registers of the 0x40080000 system block. Called from ble_219_0c045a34, which also tests the boot magic.

**Notes:** Purpose of the 3-bit fields unknown (possibly power-domain or clock source selection).

- Addresses by version: 219: 0x0C0410E8
- Peripheral registers: `0x4008005c` (RW), `0x400800b4` (RW)
- Called by: `ble_219_0c045a34`
- Confidence: low

## bes_sysreg_set_f8_low_byte

**Replace the low byte of peripheral register 0x400800f8**

Read-modify-write: 0x400800f8 = (value & 0xffffff00) | param_1. Called from ble_219_0c02ed2c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u8` | new low byte |

**Notes:** What register 0x400800f8 controls is unknown.

- Addresses by version: 219: 0x0C04124C
- Peripheral registers: `0x400800f8` (RW)
- Called by: `ble_219_0c02ed2c`
- Confidence: medium

## bes_sysreg_write_04_bit19

**Write bit 19 to 0x40080004 under BASEPRI lock, then read back 0x40080000**

Raises BASEPRI to 0x40, stores 0x80000 to 0x40080004, restores BASEPRI and performs a dummy read of 0x40080000 to flush the write. Very frequently called (about a dozen callers in the 0x0c03d000..0x0c03e100 range), and the companion at 0x0c041430 writes the same bit to 0x40080008, so the pair looks like set/clear (e.g. pulse or debug marker signal) around controller routines. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored).

**Notes:** Which of 0x40080004/0x40080008 sets versus clears, and what bit 19 drives, is unknown.

- Addresses by version: 219: 0x0C0413F0
- Peripheral registers: `0x40080000` (R), `0x40080004` (W)
- Called by: `bt_drv_reg_op_write_6byte_param`, `ble_219_0c03d69c`, `bt_drv_reg_op_env_bde4_clear_flags`, `bt_drv_reg_op_set_timing_params`, `bt_drv_reg_op_env_bde4_set_byte18`, `bt_drv_reg_op_set_rssi_monitor_params`, `ble_219_0c03df24`, `bt_drv_vco_test_start`, `bt_drv_vco_test_stop`, `bt_drv_rf_set_reg_c7c_bits13_14`, `bt_drv_reg_op_load_rssi_table_a`, `bt_drv_reg_op_load_rssi_table_b` ...
- Confidence: low

## bes_sysreg_write_04_bit4

**Write 0x10 to peripheral register 0x40080004**

Single store of 0x10 to 0x40080004. The register is written with one-hot masks by several routines (0x10, 0x100, 0x80000), so it behaves as a write-to-act (set/clear style) register of the 0x40080000 system block, which has a companion at 0x40080008. Called once from the init routine ble_219_0c03ab80.

**Notes:** Semantics of bit 4 unknown.

- Addresses by version: 219: 0x0C0410B8
- Peripheral registers: `0x40080004` (W)
- Called by: `ble_219_0c03ab80`
- Confidence: low

## bes_sysreg_write_08_bit19

**Write bit 19 to 0x40080008 under BASEPRI lock**

Raises BASEPRI to 0x40, stores 0x80000 to 0x40080008, restores BASEPRI. Counterpart of bes_sysreg_write_04_bit19; called by the same group of routines in 0x0c03d000..0x0c03e100. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is then restored).

**Notes:** Which of 0x40080004/0x40080008 sets versus clears, and what bit 19 drives, is unknown.

- Addresses by version: 219: 0x0C041430
- Peripheral registers: `0x40080008` (W)
- Called by: `bt_drv_reg_op_write_6byte_param`, `ble_219_0c03d69c`, `bt_drv_reg_op_env_bde4_clear_flags`, `bt_drv_reg_op_set_timing_params`, `bt_drv_reg_op_env_bde4_set_byte18`, `bt_drv_reg_op_set_rssi_monitor_params`, `ble_219_0c03df24`, `bt_drv_vco_test_start`, `bt_drv_vco_test_stop`, `bt_drv_rf_set_reg_c7c_bits13_14`, `bt_drv_reg_op_load_rssi_table_a`, `bt_drv_reg_op_load_rssi_table_b` ...
- Confidence: low

## ble_hw_ctrl_reg_bit1_clear

**If param_1 == 0, clear bit 1 of the register at 0x07FFA000; return 0**

Reads the 32-bit word at 0x07FFA000, ANDs it with 0xFFFFFFFD (clearing bit 1) and writes it back, only when param_1 is zero. Always returns 0. It is the inverse of ble_hw_ctrl_reg_bit1_set and is called from the same function (ble_219_0c08866c), suggesting an enable/disable pair in an ops table. The meaning of bit 1 is unknown.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | selector/channel; bit is touched only when 0 |

**Returns** `u32`: always 0

**Notes:** Read-modify-write, not atomic.

- Addresses by version: 219: 0x0C08665C
- Called by: `norflash_set_read_mode`
- Confidence: medium

## ble_hw_ctrl_reg_bit1_set

**If param_1 == 0, set bit 1 of the register at 0x07FFA000; return 0**

Reads the 32-bit word at 0x07FFA000, ORs in 0x2 and writes it back, but only when param_1 is zero; otherwise does nothing. Always returns 0. The address is in an undocumented BES region (outside the usual 0x4000xxxx peripheral window); together with its sibling that clears the same bit, it looks like an enable/disable ops-table callback invoked from ble_219_0c08866c. The meaning of bit 1 is unknown.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | selector/channel; bit is touched only when 0 |

**Returns** `u32`: always 0

**Notes:** Read-modify-write, not atomic.

- Addresses by version: 219: 0x0C086648
- Called by: `norflash_set_read_mode`
- Confidence: medium

## ble_ring_dispatch_pending

**Drain a ring of queued callbacks until the read index meets the write index**

Reads write index DAT_2000f7b0 and read index DAT_2000f7c0 (u16). While they differ it fetches entry #read from a table at DAT_2000f7b8 (8 bytes per entry: function pointer at +0, u16 value at +4) and calls fn(DAT_2000f7b4 + read * DAT_2000f7bc, entry.u16, ...), i.e. the first argument is the address of the read-th element of a parallel buffer (base DAT_2000f7b4, element size DAT_2000f7bc). Afterwards the read index is incremented and wrapped to 0 once it passes the last index DAT_2000f7be. Called from ble_219_0c0599d4 (looks like a deferred completion/event dispatch for a DMA or transport ring).

**Notes:** Exact subsystem (UART/HCI transport DMA completion vs. other event queue) not determined.

- Addresses by version: 219: 0x0C048B00
- Called by: `ble_219_0c0599d4`
- Confidence: medium

## flash_cache_hook_nop_a

**Empty stub (immediate return)**

Single-instruction function that just returns. Called together with the neighbouring empty stub from 0x0c088128, next to the flash cache invalidate routine; looks like an unused/ROM-patch hook placeholder (e.g. a pre/post flash operation callback).

**Notes:** Purpose of the hook is a guess from the caller context; the body is certain.

- Addresses by version: 219: 0x0C086BB8
- Called by: `ble_219_0c088128`
- Confidence: medium

## flash_cache_hook_nop_b

**Empty stub (immediate return)**

Single-instruction function that just returns. Companion of the other empty stub called from 0x0c088128; an unused hook placeholder.

**Notes:** Purpose of the hook is a guess from the caller context; the body is certain.

- Addresses by version: 219: 0x0C086BBC
- Called by: `ble_219_0c088128`
- Confidence: medium

## hal_analogif_reg_read

**Read a 16-bit analog/PMU/RF register over the internal SPI (ISPI) with page selection**

param_1 encodes the target: bits 15:12 select the ISPI chip/bank (written to DAT_20003D80 and programmed through hal_periph_9000_set_field_10_7 when it changes), bits 11:8 a page 0..4 (values > 4 return -1) and bits 7:0 the register number. Runs under BASEPRI 0x40 with the lock-owner trace (DAT_20003D70 = own PC 0x0c0401d2, DAT_20003D74 = caller LR when not already locked; DAT_20003D70 reset to 0xFFFFFFFF on exit). For page 0 it issues one ISPI transfer via 0x0c0326e8 with the 32-bit read command (1 << 26) | (reg << 18) and, on success, stores the received word >> 2 as the 16-bit value. For other pages it first sends the page-select word from the u16 table at 0x0c0834fc[page] << 2 through 0x0c0326c4 (ISPI send), performs the same read, then sends 0x28000 (page-select restore). Returns the ISPI result (0 = ok, value stored). Used by the many analog/PMU register helpers (0x0c02f73c ... 0x0c038250); the write counterpart is 0x0c040290.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | register address: bank << 12 \| page << 8 \| reg |
| `param_2` | `ptr` | u16 out: register value (received word >> 2) |

**Returns** `s32`: 0 on success, -1 for page > 4, otherwise the ISPI transfer status from 0x0c0326e8

**Notes:** Command encoding (read = bit 26, reg at bits 25:18, data >> 2) matches BES hal_analogif.c; 0x0c0326c4/0x0c0326e8 are assumed to be hal_ispi send/recv.

- Addresses by version: 219: 0x0C0401B0
- Called by: `ble_219_0c02f73c`, `ble_219_0c02f7d0`, `ble_219_0c02fb54`, `ble_219_0c02ffdc`, `ble_219_0c030018`, `ble_219_0c0300d0`, `ble_219_0c037a7c`, `ble_219_0c037b58`, `ble_219_0c037d08`, `ble_219_0c037f88`, `ble_219_0c038128`, `ble_219_0c038250` ...
- Calls: `hal_periph_9000_set_field_10_7`, `hal_ispi_send`, `hal_ispi_recv`
- Confidence: medium

## hal_analogif_reg_write

**Write a 16-bit analog/PMU/RF register over the internal SPI (ISPI) with page selection**

Counterpart of hal_analogif_reg_read (0x0c0401b0). param_1 bits 15:12 = ISPI bank (DAT_20003D80, re-programmed via hal_periph_9000_set_field_10_7 when it changes), bits 11:8 = page 0..4 (else return -1), bits 7:0 = register. Under BASEPRI 0x40 with the DAT_20003D70/74 lock-owner trace it sends the write word ((reg << 16) | value) << 2 with 0x0c0326c4 (ISPI send). For pages != 0 it first sends the page-select word from the u16 table at 0x0c0834fc[page] << 2 and afterwards sends 0x28000 to restore page 0. Bank 2 with a non-zero page is special: bes_iomux_reg44_clear_bits(1) is called before the sequence and bes_iomux_reg44_set_bits(1) after it (bit 0 of 0x40086044 gates that chip select). Returns the status of the data transfer. Called by the same analog/PMU helper group as the read routine.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u16` | register address: bank << 12 \| page << 8 \| reg |
| `param_2` | `u16` | value to write |
| `param_3` | `u32` | unused (register clobbered by the lock trace) |

**Returns** `s32`: 0 on success, -1 for page > 4, otherwise the ISPI send status

**Notes:** Write encoding ((reg << 16 | val) << 2) matches BES hal_analogif.c.

- Addresses by version: 219: 0x0C040290
- Called by: `ble_219_0c02f73c`, `ble_219_0c02f7d0`, `ble_219_0c02fb54`, `ble_219_0c02ffdc`, `ble_219_0c030018`, `ble_219_0c0300d0`, `ble_219_0c037a7c`, `ble_219_0c037b58`, `ble_219_0c037d08`, `ble_219_0c037f88`, `ble_219_0c038128`, `ble_219_0c038250` ...
- Calls: `hal_periph_9000_set_field_10_7`, `hal_ispi_send`, `bes_iomux_reg44_set_bits`, `bes_iomux_reg44_clear_bits`
- Confidence: medium

## hal_block_40008000_open

**Open the 0x40008000 block: enable clock and reset 0x28, program rate and mode, cache both**

Takes a config record of two words {rate, mode}. A NULL record returns -1, and an already open block (DAT_2000AA70 set) returns 0 without changes. Otherwise it sets DAT_2000AA70, raises the rate to at least 0x100, passes (rate >> 4) * 10 to RAM-patch thunk 0x20000570 and keeps the result in DAT_20003E24 (purpose not identified), enables clock id 0x28 (hal_cmu_clock_enable) and clears its reset (hal_cmu_reset_clear). It writes mode & 3 to 0x4000810C and the rate to 0x40008130, and caches the mode word in DAT_2000AA74 and the rate in DAT_2000AA78 for hal_block_40008000_set_run. It returns 0 on every open path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | config record: u32 rate (min 0x100), u32 mode (low 2 bits used) |

**Returns** `s32`: 0 on open or already open, -1 for a NULL config

- Addresses by version: 219: 0x0C0332B4
- Peripheral registers: `0x4000810c` (W), `0x40008130` (W)
- Called by: `hal_block_40008000_open_default`
- Calls: `hal_cmu_clock_enable`, `hal_cmu_reset_clear`, `ble_ram_patch_thunk_20000570`
- Confidence: high

## hal_block_40008000_open_default

**Open the 0x40008000 peripheral with the constant configuration at 0x0c081040**

Calls the driver open routine 0x0c0332b4 with the ROM config struct at 0x0c081040 ({u32 rate (min 0x100), u32 mode (low 2 bits used)}) and returns 0 regardless of the result. That routine enables clock/reset id 0x28, programs 0x4000810c and 0x40008130 and records the config at 0x2000aa74/0x2000aa78, guarded by the opened flag 0x2000aa70. No direct callers: probably invoked through an init table or callback.

**Returns** `u32`: always 0

**Notes:** Identity of the peripheral at 0x40008000 (BES-specific) is unknown.

- Addresses by version: 219: 0x0C04584C
- Calls: `hal_block_40008000_open`
- Confidence: low

## hal_block_40008000_set_run

**Start or stop the 0x40008000 block: reload mode and rate when ready, set run register**

Clears control word 0x4000812C, writes 0x0F to 0x40008108 and reads status 0x40008104. If status bit 1 is set it writes 1 to 0x40008140, the mode bits 0x4000810C from DAT_2000AA74 & 3 and the rate 0x40008130 from DAT_2000AA78, and calls RAM-patch thunks 0x20000570 and 0x20000334. It then writes 1 to 0x400081BC and 0x4000812C, and writes 0x0F (param 0, start) or 0 (nonzero, stop) to the run register 0x40008100. The two cached words are the ones stored by hal_block_40008000_open. The only caller in the packet is ble_219_0c033328.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | 0 = start (run register 0x0F), nonzero = stop (0) |

**Notes:** The identity of the 0x40008000 block is not documented anywhere in the packet.

- Addresses by version: 219: 0x0C03324C
- Peripheral registers: `0x40008000` (A), `0x40008100` (W), `0x40008104` (R), `0x40008108` (W), `0x4000810c` (W), `0x4000812c` (W), `0x40008130` (W), `0x40008140` (W), `0x400081bc` (W)
- Called by: `ble_219_0c033328`
- Calls: `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## hal_cache_enable

**Enable the cache controller at 0x07FFA000 (id 0), or pend a request if already on**

Only acts when param_1 == 0. If bit 0 of the word at 0x07FFA000 is clear it writes 1 to 0x07FFA004 and then 1 to 0x07FFA000 (init/invalidate then enable); if the cache is already enabled it writes 1 to 0x07FFA038 instead. Always returns 0. Called from the platform init routine 0x0c03ab80 together with two return-0 stubs.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | cache id, only 0 is handled |

**Returns** `u32`: always 0

**Notes:** Identification as the cache enable is a guess from the address (BES cache block) and the enable/kick sequence.

- Addresses by version: 219: 0x0C02ED04
- Called by: `ble_219_0c03ab80`
- Confidence: low

## hal_chip_select_cfg_word

**Select one of two 32-bit constants from a ROM table into DAT_20003540**

Masks param_1 to a single bit if it is greater than 1, then loads the 32-bit word at 0x0c08607c + 4*param_1 into the global DAT_20003540. The caller (chip init 0x0c03a038) passes the top two bits of a byte read from the PMU/analog chip, so the value is a variant/revision selector choosing one of two configuration constants. The constants are not decoded here.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | variant selector (0 or 1; larger values are masked with 1) |

**Notes:** Meaning of the table values and of DAT_20003540 is unknown.

- Addresses by version: 219: 0x0C02ED5C
- Called by: `ble_219_0c03a038`
- Confidence: low

## hal_cmu_aonclk9_user_disable

**Reference-counted disable of AON-CMU clock bit 9 (0x40080008 = 0x200) for user 0..3**

Counterpart of hal_cmu_aonclk9_user_enable (0x0c04146c). For user < 4: if the user map byte DAT_20003BF0 is non-zero, clears bit user; when the map becomes 0 it writes 0x200 to the AON-CMU clock-disable (clear) register 0x40080008. For user 0 it then calls the empty stub 0x0c0398a8 with (1, 0) (removed power-down hook). Users > 3 are ignored. No locking. Called from 0x0c039820.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | user id 0..3 (bit index in DAT_20003BF0) |

**Notes:** Same uncertainty about the identity of the clock as the enable routine.

- Addresses by version: 219: 0x0C0414AC
- Peripheral registers: `0x40080000` (A), `0x40080008` (W)
- Called by: `ble_219_0c039820`
- Calls: `stub_empty_0c0398a8`
- Confidence: medium

## hal_cmu_aonclk9_user_enable

**Reference-counted enable of AON-CMU clock bit 9 (0x40080004 = 0x200) for user 0..3**

Ignores users > 3. For user 0 it first calls the empty stub 0x0c0398a8 with argument 1 (a removed hook, e.g. analog power-up). If the user map byte DAT_20003BF0 is still 0 it writes 0x200 to the AON-CMU clock-enable (set) register 0x40080004, then ORs 1 << user into DAT_20003BF0. No locking. The matching disable is hal_cmu_aonclk9_user_disable (0x0c0414ac), which writes 0x200 to the clear register 0x40080008 when the last user leaves. Callers: 0x0c02fb54 (analog/PMU helper) and 0x0c03a2a0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | user id 0..3 (bit index in DAT_20003BF0) |

**Notes:** Probably the codec/audio-related clock enable of BES hal_cmu (hal_cmu_codec_clock_enable-style); the exact clock behind bit 9 is unknown.

- Addresses by version: 219: 0x0C04146C
- Peripheral registers: `0x40080004` (W)
- Called by: `ble_219_0c02fb54`, `ble_219_0c03a2a0`
- Calls: `stub_empty_0c0398a8`
- Confidence: medium

## hal_cmu_clk_block_8c_enable

**Configure and power up the clock block controlled by 0x4000008c in one of three modes (0..2)**

Rejects mode > 2 (returns 1) and returns -1 if 0x4000008c already shows an active mode (bits 0x5000 == 0x1000 or bits 0xA000 == 0x2000, i.e. a request bit 12/13 set without its matching status bit 14/15). Mode 0: power-up word 0x80, enable word 0x780, and clears bit 12 of AON-CMU 0x40080018. Modes 1 and 2 (words 0x1080/0x1780 and 0x3080/0x3780): clear bit 9 of 0x40000054, mask 0x40000018 with 0xF0FFFF08 (clears bits 27:24 and 7:3) and set bit 12 of 0x40080018. Common tail: set bits 22, 23 and 26 of 0x40080018, replace its bits 21:14 with 0x200000 (only bit 21 set), write the power-up word to 0x4000008c, delay 60 (converted by thunk 0x0c073c20, slept by thunk 0x0c073cc0 = hal_sys_timer_delay), then write the enable word (bits 10:7 set) to 0x4000008c. Returns 0. Called from the CMU setup routine 0x0c03ab80.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | mode 0, 1 or 2 (selects bits 13:12 of the 0x4000008c word) |

**Returns** `s32`: 0 ok, 1 invalid mode, -1 (0xffffffff) if the block is already active in a mode

**Notes:** Which clock this is (OSCX4, USB or audio PLL input?) is unknown; registers 0x40000018/0x54/0x8c and 0x40080018 are undocumented BES CMU/AON-CMU registers.

- Addresses by version: 219: 0x0C041264
- Peripheral registers: `0x40000018` (RW), `0x40000054` (RW), `0x4000008c` (RW), `0x40080000` (A), `0x40080018` (RW)
- Called by: `ble_219_0c03ab80`
- Calls: `ble_ram_patch_thunk_200005a8`, `ble_ram_patch_thunk_20000334`
- Confidence: low

## hal_cmu_clock_disable

**Disable the clock/gate for module id n by writing its bit to a clear register**

Returns 1 if id > 0x90. Otherwise writes 1 << (id - base) to: 0x40000004 (id < 0x20), 0x4000000C (< 0x3B), 0x40000014 (< 0x5B), 0x40000144 (< 0x67) or 0x40080044 (else). These are the +4 counterparts of the registers used by hal_cmu_clock_enable. Returns 0 on success. Called at peripheral shutdown from 0x0c030a08, 0x0c031ea4 and 0x0c033acc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | module id (0..0x90) |

**Returns** `u32`: 0 on success, 1 if the id is out of range

**Notes:** See hal_cmu_clock_enable regarding the interpretation.

- Addresses by version: 219: 0x0C04070C
- Peripheral registers: `0x40000004` (W), `0x4000000c` (W), `0x40000014` (W), `0x40000144` (W), `0x40080044` (W)
- Called by: `hal_i2c_close_internal`, `ble_219_0c031ea4`, `hal_uart_close_internal`
- Confidence: medium

## hal_cmu_clock_enable

**Enable the clock/gate for module id n by writing its bit to a set register**

Returns 1 if id > 0x90. Otherwise writes 1 << (id - base) to the 'set' register of the matching bank: id < 0x20 -> 0x40000000; < 0x3B -> 0x40000008; < 0x5B -> 0x40000010; < 0x67 -> 0x40000140; else 0x40080040 (then dummy-reads 0x40080000 to flush the write). Returns 0 on success. The paired clear registers are +4 (see hal_cmu_clock_disable). Called by peripheral bring-up code at 0x0c0321f8, 0x0c0332b4, 0x0c034008 and 0x0c0458a6 together with hal_cmu_reset_clear.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | module id (0..0x90) |

**Returns** `u32`: 0 on success, 1 if the id is out of range

**Notes:** Clock gate interpretation is based on the Bestechnic CMU register convention (ENABLE/DISABLE pairs); not confirmed against documentation.

- Addresses by version: 219: 0x0C040690
- Peripheral registers: `0x40000000` (W), `0x40000008` (W), `0x40000010` (W), `0x40000140` (W), `0x40080000` (R), `0x40080040` (W)
- Called by: `hal_spi_open_common`, `hal_block_40008000_open`, `ble_219_0c034008`, `ble_219_0c0458a6`
- Confidence: medium

## hal_cmu_clock_is_enabled

**Return whether the clock/gate bit of module id n is currently set**

Returns false if id > 0x90. Otherwise reads the status register of the matching bank (0x40000000, 0x40000008, 0x40000010, 0x40000144, 0x40080040) and returns whether the bit (id - bank base) is set. Note the 4th bank is read at 0x40000144 (the clear register address) while hal_cmu_clock_enable writes 0x40000140, so this read-back address follows the hardware's status layout. Called from 0x0c033ca8 and 0x0c034008.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | module id (0..0x90) |

**Returns** `bool`: true if the module's clock bit reads set

**Notes:** Bank-4 read address (0x40000144) differs from the set register used by the enable function; may be a hardware quirk or a different register meaning.

- Addresses by version: 219: 0x0C040784
- Peripheral registers: `0x40000000` (R), `0x40000008` (R), `0x40000010` (R), `0x40000144` (R), `0x40080040` (R)
- Called by: `hal_uart_set_baud_rate`, `ble_219_0c034008`
- Confidence: medium

## hal_cmu_get_crystal_freq

**Return the nominal crystal frequency, 24000000 Hz**

Returns the constant 24,000,000. The chip init routine 0x0c03a038 compares it with a measured value from 0x0c073c50 and, if different, computes a ratio against 24000000 and calls a trimming routine.

**Returns** `u32`: crystal frequency in Hz (24 MHz)

- Addresses by version: 219: 0x0C02ED78
- Called by: `ble_219_0c03a038`
- Confidence: high

## hal_cmu_osc_x2_enable

**Power up the crystal x2 clock (0x40000060 = 0x4000), wait 60 us, then enable it (0x2000)**

Writes 0x4000 to the CMU set register 0x40000060 (power-up bit of the OSCX2 block), converts 60 (us) to sys-timer ticks through the RAM thunk 0x0c073c20 and delays that long via the RAM thunk 0x0c073cc0 (hal_sys_timer_delay), then writes 0x2000 to 0x40000060 (clock-enable bit). Mirrors BES hal_cmu_osc_x2_enable(): CMU_PU_OSCX2_ENABLE, delay US_TO_TICKS(60), CMU_EN_OSCX2_ENABLE. Called once from the CMU setup routine 0x0c03ab80.

**Notes:** Bit meanings taken from the BES hal_cmu source pattern; 0x40000060 is the CMU 'set' register also used by bes_cmu_bit29/30_ctrl.

- Addresses by version: 219: 0x0C0410C4
- Peripheral registers: `0x40000060` (W)
- Called by: `ble_219_0c03ab80`
- Calls: `ble_ram_patch_thunk_200005a8`, `ble_ram_patch_thunk_20000334`
- Confidence: medium

## hal_cmu_pll_enable

**Power up and enable PLL 0..2 for a user id with reference counting in DAT_20003D84[]**

Selects per-PLL constants: pll 0 -> power-up 0x4000, lock-check mask 0x1000, enable bit 0x1, PLL-select 1; pll 1 -> 0x800, 0x8000, 0x400, 2; else -> 0x8000, 0x2000, 0x20, 4. Under BASEPRI 0x40 (lock-owner trace in DAT_20003D70/74): if no user holds the PLL (byte DAT_20003D84[pll] == 0) or user == 5 (HAL_CMU_PLL_USER_ALL) it powers it up - writing 0x40000 to CMU 0x40000060 when the PLL is the selected clock source (DAT_2000354D == pll, see hal_cmu_select_pll_source) or the power-up constant to AON-CMU 0x40080004 otherwise - then delays 20 units via the RAM thunk 0x0c073ae0 and sets bit user in the user map (unless user == 5). If already powered it only sets the user bit and clears the lock-check mask. It then polls for up to 200 (converted by thunk 0x0c073c20) sys-timer ticks: with no check mask it waits for 0x40000060 bit 17 or 0x40080004 & enable bit; with a check mask it reads 0x4008004c each pass. Finally it enables the clock (0x40000060 = 0x20000 or 0x40080004 = enable bit), writes the PLL-select value to 0x400800a0 and returns 0 if 0x4008004c & check-mask is set, else 2. Called from 0x0c040cfc; counterpart hal_cmu_pll_release_user (0x0c0405f4) uses the same constants.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | PLL id 0..2 (index into DAT_20003D84[]) |
| `param_2` | `u32` | user id bit 0..4, 5 = all users |

**Returns** `u32`: 0 if the lock bit (0x4008004c & mask) is set, 2 otherwise (also when the PLL was already in use, since the mask is zeroed)

**Notes:** Structure matches BES hal_cmu_pll_enable(). In the decompilation the check-mask branch of the poll loop never breaks early; this may be a decompiler artefact.

- Addresses by version: 219: 0x0C0404AC
- Peripheral registers: `0x40000000` (A), `0x40000060` (RW), `0x40080000` (A), `0x40080004` (RW), `0x4008004c` (R), `0x400800a0` (W)
- Called by: `hal_cmu_sys_pll_restart`
- Calls: `ble_ram_patch_thunk_20000348`, `ble_ram_patch_thunk_2000031c`, `ble_ram_patch_thunk_200005a8`
- Confidence: medium

## hal_cmu_pll_release_user

**Clear a user bit for clock source n and power it down when the last user is gone**

For param_1 = 0/1/other selects constants (0x1,0x4000,0x1 / 0x2,0x800,0x400 / 0x4,0x8000,0x20). Inside a BASEPRI 0x40 critical section (with the same DAT_20003d70/74 owner-debug bookkeeping as 0x0c040450) it clears bit param_2 in the per-source user mask byte DAT_20003d84[param_1] (param_2 == 5 forces release without checking). When the mask becomes 0 it writes the first constant to 0x400800A4 and, if DAT_2000354D equals param_1 (this source is the selected one), writes 0x20000 then 0x40000 to 0x40000064; otherwise writes the other two constants to 0x40080008. Returns 0.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | clock source / PLL index (0, 1, other) |
| `param_2` | `u32` | user id bit to release (0..4); 5 releases unconditionally |

**Returns** `u32`: always 0

**Notes:** Looks like a reference-counted clock/PLL disable; actual hardware identity of the registers is unknown.

- Addresses by version: 219: 0x0C0405F4
- Peripheral registers: `0x40000064` (W), `0x40080008` (W), `0x400800a4` (W)
- Called by: `hal_cmu_sys_pll_restart`
- Confidence: low

## hal_cmu_reset_clear

**Release (clear) the reset bit of module id n**

Returns 1 if id > 0x99. Otherwise writes 1 << (id - base) to the clear-side registers: 0x40000038 (id < 0x20), 0x40000040 (< 0x3B), 0x40000048 (< 0x5B), 0x40000154 (< 0x67), 0x40080014 (< 0x91) or 0x400800CC (else); for the last two banks it also dummy-reads 0x40080000 to flush the write. Counterpart to hal_cmu_reset_set. Called at peripheral start-up from 0x0c0321f8, 0x0c0332b4, 0x0c034008, 0x0c040934 and 0x0c0458a6.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | module id (0..0x99) |

**Returns** `u32`: 0 on success, 1 if the id is out of range

**Notes:** Reset semantics inferred from call pairing.

- Addresses by version: 219: 0x0C040890
- Peripheral registers: `0x40000038` (W), `0x40000040` (W), `0x40000048` (W), `0x40000154` (W), `0x40080000` (R), `0x40080014` (W), `0x400800cc` (W)
- Called by: `hal_spi_open_common`, `hal_block_40008000_open`, `ble_219_0c034008`, `hal_cmu_reset_pulse_nocheck`, `ble_219_0c0458a6`
- Confidence: medium

## hal_cmu_reset_get_state

**Test whether the reset/gate bit of module id n is set in the 0x40000034.. status registers**

Maps a module id to a bit in a bank of registers: id < 0x20 -> 0x40000034 bit id; < 0x3B -> 0x4000003C bit id-0x20; < 0x5B -> 0x40000044 bit id-0x3B; < 0x67 -> 0x40000150 bit id-0x5B; < 0x91 -> 0x40080010 bit id-0x67; otherwise 0x400800C8 bit id-0x91. Returns true if that bit is set. These registers are the 'set' side of the pair written by hal_cmu_reset_set (0x0c040804) and cleared by hal_cmu_reset_clear (0x0c040890), so this reads the current software-reset assertion state of a peripheral. Called from 0x0c040934.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | module/peripheral id (0..0x99) |

**Returns** `bool`: true if the bit for that module is set

**Notes:** Naming follows the Bestechnic SDK CMU convention; register semantics (reset vs clock) are inferred from the set/clear register pattern and call sites.

- Addresses by version: 219: 0x0C0403C8
- Peripheral registers: `0x40000034` (R), `0x4000003c` (R), `0x40000044` (R), `0x40000150` (R), `0x40080010` (R), `0x400800c8` (R)
- Called by: `hal_cmu_reset_pulse_nocheck`
- Confidence: medium

## hal_cmu_reset_pulse

**Range-check a CMU module id (<= 0x99) and pulse its reset line**

Public entry of the reset-pulse operation: returns 1 for module ids above 0x99, otherwise continues into hal_cmu_reset_pulse_nocheck (0x0c040934), whose body the decompiler has duplicated here: if hal_cmu_reset_get_state(id) reports the module held in reset it just calls hal_cmu_reset_clear(id); otherwise it writes 1 << (id - base) to the *_RESET_PULSE register of the bank the id falls in (0x40000028 for id < 0x20, 0x4000002c for < 0x3B, 0x40000030 for < 0x5B, 0x4000014c for < 0x67, AON-CMU 0x4008000c for < 0x91, 0x400800c4 above; the AON banks are followed by three dummy reads of 0x40080000), spins a 3-iteration delay loop and returns 0. Same bank split as hal_cmu_reset_get_state/hal_cmu_reset_clear (set side 0x34/0x3c/0x44/0x150/0x40080010/0x400800c8, clear side 0x38/0x40/0x48/0x154/0x40080014/0x400800cc). Called from 0x0c032408.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | HAL_CMU module id 0..0x99 |

**Returns** `u32`: 1 for an invalid id, otherwise the result of the pulse routine (0, or hal_cmu_reset_clear's result)

**Notes:** Register names follow the BES reg_cmu layout (HRESET/PRESET/ORESET_PULSE at 0x28/0x2c/0x30).

- Addresses by version: 219: 0x0C04092C
- Called by: `ble_219_0c032408`
- Calls: `hal_cmu_reset_pulse_nocheck`
- Confidence: medium

## hal_cmu_reset_pulse_nocheck

**Pulse the software reset of CMU module id (no range check), or release it if currently held in reset**

Body of hal_cmu_reset_pulse (0x0c04092c) without the id range check. Calls hal_cmu_reset_get_state(id); if the module's reset bit is not set it returns hal_cmu_reset_clear(id) instead of pulsing. Otherwise writes a one-hot bit to the pulse register of the bank containing id: 0x40000028 bit id (id < 0x20), 0x4000002c bit id-0x20 (< 0x3B), 0x40000030 bit id-0x3B (< 0x5B), 0x4000014c bit id-0x5B (< 0x67), AON-CMU 0x4008000c bit id-0x67 (< 0x91) or 0x400800c4 bit id-0x91; for the two AON banks it reads 0x40080000 three times to flush the write. A volatile 3-iteration loop gives the hardware a few cycles before returning 0. Part of the hal_cmu reset group with hal_cmu_reset_set (0x0c040804), hal_cmu_reset_clear and hal_cmu_reset_get_state.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | HAL_CMU module id (caller guarantees <= 0x99) |

**Returns** `u32`: 0 after pulsing, or hal_cmu_reset_clear's result when the module was in reset

**Notes:** Which polarity of the status bit means 'in reset' depends on the BES set/clear convention; the code calls reset_clear when get_state returns 0.

- Addresses by version: 219: 0x0C040934
- Peripheral registers: `0x40000028` (W), `0x4000002c` (W), `0x40000030` (W), `0x4000014c` (W), `0x40080000` (R), `0x4008000c` (W), `0x400800c4` (W)
- Called by: `hal_cmu_reset_pulse`
- Calls: `hal_cmu_reset_get_state`, `hal_cmu_reset_clear`
- Confidence: medium

## hal_cmu_reset_set

**Assert (set) the reset bit of module id n**

Returns 1 if id > 0x99. Otherwise writes 1 << (id - base) to: 0x40000034 (id < 0x20), 0x4000003C (< 0x3B), 0x40000044 (< 0x5B), 0x40000150 (< 0x67), 0x40080010 (< 0x91) or 0x400800C8 (else). These registers are read back by hal_cmu_reset_get_state (0x0c0403c8) and cleared by hal_cmu_reset_clear (0x0c040890). Called at peripheral shutdown (0x0c02ed80, 0x0c030a08, 0x0c031ea4, 0x0c033acc) together with the clock disable.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | module id (0..0x99) |

**Returns** `u32`: 0 on success, 1 if the id is out of range

**Notes:** Reset semantics inferred from call pairing (set on shutdown, clear on start-up with clock enable).

- Addresses by version: 219: 0x0C040804
- Peripheral registers: `0x40000034` (W), `0x4000003c` (W), `0x40000044` (W), `0x40000150` (W), `0x40080010` (W), `0x400800c8` (W)
- Called by: `hal_cmu_reset_set_mod99`, `hal_i2c_close_internal`, `ble_219_0c031ea4`, `hal_uart_close_internal`
- Confidence: medium

## hal_cmu_reset_set_mod99

**Assert the CMU software reset of module id 0x99 (bit 8 of 0x400800c8)**

Calls hal_cmu_reset_set(0x99). Per the id-to-register mapping used by hal_cmu_reset_get_state, id 0x99 (153) falls in the last bank (ids >= 0x91 -> register 0x400800c8, bit 0x99-0x91 = 8), i.e. a module in the 0x40080000 'AON' CMU block. Single caller 0x0c039820, a power-down sequence run under a BASEPRI critical section (system clock config 3, PMU/analog writes 0xcafe/0x5fee to register 0x3000 through the analog interface, then this reset), so the module is most likely the Bluetooth/BLE subsystem being held in reset when the radio is powered down.

**Notes:** Identity of module 0x99 (probably the BT core: BES hal_cmu_bt_reset_set) is a guess from the caller's context.

- Addresses by version: 219: 0x0C02ED80
- Called by: `ble_219_0c039820`
- Calls: `hal_cmu_reset_set`
- Confidence: medium

## hal_cmu_select_pll_source

**Record the active clock source index and program bits 18:17 of 0x40000070 inside a critical section**

Maps param_1 (0, 1, other) to a field value 0, 0x20000, 0x60000 and, under BASEPRI 0x40 (if not already in a critical section it stores the caller LR/address in DAT_20003d70/DAT_20003d74 for lock-owner debugging, and resets DAT_20003d70 to 0xFFFFFFFF on exit), stores param_1 in byte DAT_2000354D and updates 0x40000070 = (0x40000070 & 0xFFF9FFFF) | field. Restores BASEPRI and returns 0. Caller is 0x0c040cfc, which also calls hal_cmu_pll_release_user (0x0c0405f4).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | clock-source / PLL index (0, 1, or any other value meaning 2) |

**Returns** `u32`: always 0

**Notes:** Interpretation as PLL source select is a guess from pairing with 0x0c0405f4; 0x40000070 semantic is not documented.

- Addresses by version: 219: 0x0C040450
- Peripheral registers: `0x40000070` (RW)
- Called by: `hal_cmu_sys_pll_restart`
- Confidence: low

## hal_cmu_sys_pll_restart

**Release all users of PLL 0, reselect source 0, clear 0x4000010c bits 31:30 and re-enable PLL 0**

Clock re-initialisation step used by the CMU setup routine 0x0c03ab80. Sequence: hal_cmu_pll_release_user(0, 5) (5 = all users, powers PLL 0 down), hal_cmu_select_pll_source(0), then under BASEPRI 0x40 with the DAT_20003D70/74 lock-owner trace clears bits 31:30 of CMU register 0x4000010c (read-modify-write with mask 0x3FFFFFFF), then hal_cmu_pll_enable(0, <user not visible in the decompilation, r1 left over>) to power PLL 0 back up, and finally bes_cmu_bit29_ctrl() and bes_cmu_bit30_ctrl(0), which write 0x20000000 and 0x40000000 to the CMU set register 0x40000060. Always returns 0. Only caller: 0x0c03ab80.

**Returns** `u32`: always 0

**Notes:** Purpose (PLL re-lock after crystal/frequency change?) inferred only from the call sequence; the argument passed in r1 to hal_cmu_pll_enable is not shown by the decompiler.

- Addresses by version: 219: 0x0C040CFC
- Peripheral registers: `0x4000010c` (RW)
- Called by: `ble_219_0c03ab80`
- Calls: `hal_cmu_select_pll_source`, `hal_cmu_pll_enable`, `hal_cmu_pll_release_user`, `bes_cmu_bit29_ctrl`, `bes_cmu_bit30_ctrl`
- Confidence: low

## hal_ext_ctrl_write_d0702000

**Write 1 and 2 to the two control words at 0xd0702000/0xd0702004**

Stores 1 into the word at 0xd0702000 and 2 into 0xd0702004. These addresses are outside the usual 0x4000xxxx peripheral window (an external/aliased bus region of the SoC), so the purpose is not determinable from the code. Called once from the init routine at 0x0c03bb70.

**Notes:** Target region 0xd0702000 is undocumented; may be a memory controller or boot-time hardware enable.

- Addresses by version: 219: 0x0C03AA64
- Called by: `ble_219_0c03bb70`
- Confidence: low

## hal_gpadc_adc2volt

**Convert a raw GPADC code to a calibrated voltage (two-point calibration from efuse, lazily initialised)**

On first use (DAT_2000a5e1 == 0) it fetches the two calibration codes with 0x0c03a1b0 (efuse-derived values or defaults 0x32f0/0x4330 when no efuse data), substitutes 13099.0 for a zero first code and 17230.0 for a zero second code, and computes slope DAT_2000a5e8 = 200 / (c2 - c1) and intercept DAT_2000a5e4 = (640*c2 - 840*c1) / (c2 - c1); this maps code c1 to 640 and c2 to 840, i.e. the two calibration points are the ADC readings at 640 and 840 (mV). Then DAT_2000a5e1 is set to 1. For every call: if param_1 == 0xffff (HAL_GPADC_BAD_VALUE) it is returned unchanged; otherwise result = (float)param_1 * slope + intercept, negative results are clamped to 0 and the value is truncated to 16 bits. Uses VFP single precision. No direct callers (used through a function pointer / ADC task).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | raw ADC code (16-bit), or 0xffff for 'bad value' |

**Returns** `u32`: calibrated value, probably millivolts, 0..0xffff

**Notes:** Unit (mV) and the efuse origin of the codes are inferred from the 640/840 reference values and the BES hal_gpadc conventions; the helper 0x0c03a1b0 masks two efuse words to 11 bits and adds 12000 / 16200.

- Addresses by version: 219: 0x0C02F810
- Calls: `bes_calib_get_trim_pair`
- Confidence: medium

## hal_gpdma_cancel

**Stop a GPDMA channel and clear its pending interrupt flags**

param_1 is a channel id (bit4 = controller 0/1, low 3 bits = channel; ids >= 0x20 or with bit 3 set hang in an assert loop). Clears the enable bit (bit 0) of the channel config register at ctrl + ch*0x20 + 0x110, then writes the channel bit to the TC-clear (+8) and error-clear (+0x10) registers of the controller. Does not release the channel allocation flag.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | channel id: controller<<4 \| channel |

- Addresses by version: 219: 0x0C02F354
- Called by: `hal_gpdma_stop`, `hal_gpdma_free_chan`, `hal_spi_dma_cancel_all`, `ble_219_0c031ea4`, `hal_spi_dma_tx_done_handler`, `ble_219_0c032408`, `hal_uart_close_internal`
- Confidence: high

## hal_gpdma_chan_busy

**Return whether a GPDMA channel is currently enabled/running**

param_1 is a channel id (controller<<4 | channel; invalid values hang in an assert loop). Reads the controller's enabled-channels register (ctrl+0x1c) and returns true if the channel's bit is set.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | channel id |

**Returns** `bool`: true if the channel is active

- Addresses by version: 219: 0x0C02F5DC
- Called by: `ble_219_0c032408`, `hal_spi_dma_rx_start`, `hal_uart_tx_dma_busy`, `hal_uart_rx_dma_busy`
- Confidence: high

## hal_gpdma_chan_irq_handler

**Service one GPDMA channel interrupt: clear TC/error flags and invoke the user callback**

param_1 selects one of two PL080-style DMA controllers (base pointers table at 0x0c080a00, i.e. 0x40120000 and 0x40130000) and param_2 the channel (0..7). Builds mask = 1<<channel; if the terminal-count status (ctrl+4) bit is set it writes the bit to the TC-clear register (ctrl+8); reads the error status (ctrl+0xc) and, when set, writes it to the error-clear register (ctrl+0x10). Then fetches the callback from the table at 0x2000a5a0[param_1*8+param_2] and, if non-NULL, calls it with (channel id = param_2 | param_1<<4, remaining transfer size = channel control reg (+0x10c) & 0xfff, error flag, current LLI pointer (+0x108)). Called from the DMA IRQ vector wrappers (IRQ3_Handler 0x0c04555c and the next handler 0x0c04556c).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | DMA controller index (0 or 1) |
| `param_2` | `u32` | channel number 0..7 within the controller |

**Notes:** Register offsets match the ARM PrimeCell PL080 layout; the BES SDK name is hal_gpdma.c (hal_gpdma_irq_handler).

- Addresses by version: 219: 0x0C02EECC
- Called by: `hal_dma0_irq_handler`, `hal_dma1_irq_handler`
- Confidence: high

## hal_gpdma_free_chan

**Cancel a GPDMA channel and release it (clear allocation flag and its sync bit in the controller config)**

param_1 is a channel id (controller << 4 | channel); ids >= 0x20 or with bit 3 set hang in an assert loop, as does freeing a channel whose allocation flag DAT_2000a548[ctrl*8+ch] is 0. Calls hal_gpdma_cancel(param_1) to stop the channel, then inside a BASEPRI critical section (BASEPRI raised to 0x40 when privileged; if it was not already 0x40 the call-site address 0x0c02f590 and LR are logged to DAT_20003d70/DAT_20003d74, DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0, BASEPRI restored afterwards) clears the allocation flag and clears bit (12 + ch) in the controller configuration register (+0x30), undoing what hal_gpdma_get_chan set. Counterpart of hal_gpdma_get_chan; called by the SPI DMA done/cancel handlers and the UART DMA routines (12 callers).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | GPDMA channel id (controller << 4 \| channel 0..7) |

- Addresses by version: 219: 0x0C02F558
- Called by: `hal_spi_dma_cancel_all`, `ble_219_0c031ea4`, `hal_spi_dma_rx_done_handler`, `hal_spi_dma_tx_done_handler`, `ble_219_0c032408`, `hal_spi_dma_rx_start`, `hal_uart_tx_dma_complete`, `hal_uart_rx_dma_complete`, `hal_uart_tx_dma_start_sg`, `hal_uart_close_internal`, `hal_uart_tx_dma_stop`, `hal_uart_rx_dma_start`
- Calls: `hal_gpdma_cancel`
- Confidence: high

## hal_gpdma_get_chan

**Allocate a free GPDMA channel for a peripheral**

param_2 > 2 hangs (assert); param_1 == 0 returns 0xff. The peripheral id param_1 is mapped to a controller (ids 1..3: controller = (id == 2); other ids are looked up in two ROM byte tables, assert if absent). The channel range of that controller comes from the byte tables 0x0c080738 (first) and 0x0c08073c (count). Under a BASEPRI critical section it scans the range: policy 0 ascending (lowest channel first), policy 1 descending, policy 2 descending but only the top two channels. A channel is taken when its flag in DAT_2000a548[ctrl*8+ch] is 0 and its enable bit in ctrl+0x1c is clear; it then sets the flag, ORs (1<<ch)<<12 into the controller config register (+0x30), and records the caller's LR in the table at 0x2000a558. Returns controller<<4 | channel or 0xff when none is free.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | peripheral/request id (0 = none) |
| `param_2` | `u32` | channel selection policy 0..2 |

**Returns** `u32`: channel id (controller<<4 | channel) or 0xff if none

**Notes:** Policy meanings derived from the scan order; the BES enum (HAL_DMA_HIGH_PRIO etc.) names were not checked.

- Addresses by version: 219: 0x0C02F41C
- Called by: `ble_219_0c032408`, `hal_spi_dma_rx_start`, `hal_uart_tx_dma_start_sg`, `hal_uart_rx_dma_start`
- Confidence: medium

## hal_gpdma_get_sg_remain_size

**Return the total number of units still to transfer on a GPDMA channel**

For channel id param_1, starts from the remaining count in the channel control register (+0x10c & 0xfff), then follows the linked list beginning at the LLI pointer in +0x108, adding the size field (word3 & 0xfff) of every descriptor until the next pointer is NULL or loops back to the first descriptor. Called from the DMA consumers 0x0c033530, 0x0c033610 and 0x0c033bd8 to compute remaining/received length.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | channel id |

**Returns** `u32`: sum of remaining transfer sizes (units of the channel's transfer width)

- Addresses by version: 219: 0x0C02F610
- Called by: `hal_uart_tx_dma_complete`, `hal_uart_rx_dma_complete`, `hal_uart_tx_dma_stop`
- Confidence: high

## hal_gpdma_init

**One-time initialisation of both GPDMA controllers**

If DAT_2000a59c is 0: for each controller (0x40120000 and 0x40130000) writes 0xffffffff to the TC-clear (+8) and error-clear (+0x10) registers, sets the config register (+0x30) to (old & 0x7ff00ff0) | 9, then zeroes the eight channel config registers (+0x110 + n*0x20). Marks DAT_2000a59c = 1 and clears the four words 0x2000a548..0x2000a554 (the 16 channel-allocated flags). Called from the platform init routine 0x0c0459d4.

- Addresses by version: 219: 0x0C02F6A4
- Called by: `ble_219_0c0459d4`
- Confidence: high

## hal_gpdma_init_desc

**Fill a 4-word GPDMA linked-list descriptor from a channel configuration**

param_2 is the HAL DMA channel config. The function validates it (transfer size at +2 must be <= 0xfff, bits 3..5 of the type byte at +8 must be 0, otherwise returns 1) and builds a PL080 LLI: word0 = source address, word1 = destination address, word2 = param_3 (next descriptor pointer), word3 = control = size[11:0] | src burst (+6)<<12 | dst burst (+7)<<15 | src width (+4)<<18 | dst width (+5)<<21 | transfer-type bits from the ROM table at 0x0c074588 | 0x4000000 (src increment, cfg bit6) | 0x8000000 (dst increment, cfg bit7) | 0x80000000 if param_4 (terminal-count interrupt). For a peripheral source/destination (type not memory) the address is looked up by the peripheral id at cfg+9 / cfg+10 in two ROM id tables and then in the FIFO address table at 0x0c080bd8; otherwise the plain addresses at cfg+0xc / cfg+0x10 are used. Returns the invalid-bit check result (0 on success). Called from several DMA users (0x0c02f330, 0x0c032954, 0x0c0336b0, 0x0c033e04).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output descriptor (4 x u32) |
| `param_2` | `ptr` | HAL_DMA_CH_CFG-style channel configuration |
| `param_3` | `u32` | next descriptor address (0 for last) |
| `param_4` | `s32` | non-zero to raise a terminal-count interrupt for this descriptor |

**Returns** `u32`: 0 on success, non-zero (1 or the invalid type bits) on a bad config

**Notes:** Mirrors BES hal_gpdma_init_desc. The two peripheral-id lookup loops are decompiled poorly (they scan a byte table that overlaps a string literal), so which peripheral ids map to which FIFO address is not decoded.

- Addresses by version: 219: 0x0C02EF3C
- Called by: `hal_gpdma_start`, `hal_spi_dma_rx_start`, `hal_uart_tx_dma_start_sg`, `hal_uart_rx_dma_start`
- Confidence: medium

## hal_gpdma_sg_start

**Program a GPDMA channel with a descriptor and config, then start it**

param_1 is the first LLI (4 words), param_2 the channel config (byte0 = channel id: bit4 selects the controller, low 3 bits the channel; bytes 9/10 = source/dest peripheral ids; +0x14 = completion callback; +0x18 = optional start callback), param_3/param_4 optional 2-D (source/destination) rectangle descriptors. Asserts (infinite loop) on an invalid channel id or a peripheral that does not belong to the channel's controller. If the channel was allocated (DAT_2000a548 flag) and is not already enabled (ctrl+0x1c), it stores the callback in 0x2000a5a0, clears pending TC/err flags, writes the LLI to channel regs +0x100..+0x10c, builds the config word at +0x110 (interrupt enables 0xc000 if a callback exists, src periph<<1, dst periph<<6, flow control<<11, bit 19 if cfg byte1 != 0), programs the optional 2-D registers at +0x200..+0x20c and flags in +0x210, calls the start callback with the channel id under a BASEPRI critical section, and finally sets the enable bit (+0x110 |= 1). Returns 0 on success, 1 if the channel is unallocated or busy.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first linked-list descriptor (src, dst, next, control) |
| `param_2` | `ptr` | channel configuration structure |
| `param_3` | `ptr` | optional source 2-D config (4 x s16) or NULL |
| `param_4` | `ptr` | optional destination 2-D config (4 x s16) or NULL |

**Returns** `u32`: 0 = started, 1 = channel not allocated or already busy

**Notes:** Mirrors BES hal_gpdma_sg_start; the meaning of config bit 19 and of the 2-D registers (offsets 0x200-0x210) is inferred only from the code.

- Addresses by version: 219: 0x0C02F098
- Called by: `hal_gpdma_sg_start_linear`, `hal_gpdma_start`
- Confidence: medium

## hal_gpdma_sg_start_linear

**Start a scatter-gather GPDMA transfer without 2-D descriptors (hal_gpdma_sg_start(desc, cfg, NULL))**

Thin wrapper: hal_gpdma_sg_start(param_1, param_2, 0), i.e. the linked-list descriptor chain param_1 is started on the channel described by param_2 with no 2-D source/destination rectangle descriptors. Return value of the underlying call (0 ok, 1 if the channel is unallocated or busy) is discarded. Callers are the UART DMA paths 0x0c032954, 0x0c0336b0 and 0x0c033e04. Corresponds to the two-argument hal_gpdma_sg_start of the BES SDK, which forwards to the 2-D variant with NULL rectangles.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | first 4-word GPDMA linked-list descriptor |
| `param_2` | `ptr` | channel configuration (byte 0 = channel id, +0x14 callback) |

- Addresses by version: 219: 0x0C02F328
- Called by: `hal_spi_dma_rx_start`, `hal_uart_tx_dma_start_sg`, `hal_uart_rx_dma_start`
- Calls: `hal_gpdma_sg_start`
- Confidence: high

## hal_gpdma_start

**Start a single-descriptor GPDMA transfer from a channel configuration**

Builds one 4-word linked-list descriptor on the stack with hal_gpdma_init_desc(desc, param_1, next = 0, tc_irq = 1) and, when that returns 0, programs and starts the channel with hal_gpdma_sg_start(desc, param_1) (no 2-D descriptors). Because the descriptor lives on the stack, this is only valid for transfers whose descriptor the hardware has already latched before return, which is how the BES SDK hal_gpdma_start is written as well. Errors from either step are silently ignored. Callers: the SPI DMA transfer 0x0c032408 and the UART DMA routine 0x0c033e04.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | GPDMA channel configuration (src/dst addresses, size, channel id, callbacks) |

- Addresses by version: 219: 0x0C02F330
- Called by: `ble_219_0c032408`, `hal_uart_rx_dma_start`
- Calls: `hal_gpdma_init_desc`, `hal_gpdma_sg_start`
- Confidence: high

## hal_gpdma_stop

**Halt a GPDMA channel, wait (up to 10 tries) for it to go inactive, then cancel it**

param_1 is a channel id (controller << 4 | channel, 0..7); values >= 0x20 or with bit 3 set hang in an assert loop. Locates the channel register block (controller base from table 0x0c080a00 + channel * 0x20) and sets bit 18 (HALT) in the channel configuration register (+0x110). While bit 17 (ACTIVE) stays set it retries up to 10 times: tries 2..4 busy-wait via the RAM-patch delay thunk 0x20000348 with argument 10; later tries sleep instead: if no sleep hook is registered in DAT_2000a598 or the code runs inside an exception (IPSR != 0), it waits 1 unit via thunk 0x20000570(1) followed by thunk 0x20000334, otherwise it calls the hook (*DAT_2000a598)(1) (an OS delay/yield callback usable only from thread mode). Finally calls hal_gpdma_cancel(param_1), which disables the channel and clears its pending interrupt flags. Matches the PL080 recommended stop sequence (halt, wait for FIFO drain, disable). Single caller 0x0c033bd8 (UART DMA RX stop, which then reads the remaining size).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | GPDMA channel id (controller << 4 \| channel 0..7) |

**Notes:** Exact units of the two delay thunks (ticks vs ms) are not confirmed.

- Addresses by version: 219: 0x0C02F390
- Called by: `hal_uart_tx_dma_stop`
- Calls: `hal_gpdma_cancel`, `ble_ram_patch_thunk_20000348`, `ble_ram_patch_thunk_20000570`, `ble_ram_patch_thunk_20000334`
- Confidence: high

## hal_hwsem_try_lock

**Read hardware semaphore register n (0..3) at 0x400000C0**

If param_1 < 4 returns the word at 0x40000000 + (param_1 + 0x30)*4 (= 0x400000C0 + 4*n), else 0. The TRNG read routine 0x0c033328 polls it with index 1 until it returns non-zero before touching the TRNG block, then releases it with hal_hwsem_unlock, so a non-zero read means the lock was acquired.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | semaphore index 0..3 |

**Returns** `u32`: register value (non-zero = acquired) or 0 for an invalid index

**Notes:** Take-on-read semantics inferred from the polling loop in the caller.

- Addresses by version: 219: 0x0C0319DC
- Peripheral registers: `0x40000000` (A)
- Called by: `ble_219_0c033328`
- Confidence: medium

## hal_hwsem_unlock

**Write 1 to hardware semaphore register n (0..3) at 0x400000C0 to release it**

If param_1 < 4 writes 1 to 0x40000000 + (param_1 + 0x30)*4; otherwise does nothing. Called by the TRNG routine 0x0c033328 on exit (index 1).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | semaphore index 0..3 |

**Notes:** Counterpart of hal_hwsem_try_lock.

- Addresses by version: 219: 0x0C0319F0
- Peripheral registers: `0x40000000` (A)
- Called by: `ble_219_0c033328`
- Confidence: medium

## hal_i2c_calc_scl_cnt

**Compute SCL high/low counts for an I2C bus speed from timing minima**

Works in clock ticks: min_high = ceil(param_5*param_2/1000) forced to at least param_4+8, min_low = ceil(param_5*param_3/1000) forced to at least 2*param_4+11 (param_4 looks like the spike-filter length). If the total period param_1 is smaller than min_high+min_low the high count is min_high-1; otherwise the spare time is shared so that both phases get at least half the period rounded up (balancing toward the shorter one). Outputs *param_6 = high count - 1 and *param_7 = low count - param_4 - 6; a result that does not fit in 16 bits hangs in an assert loop. Called from 0x0c0458a6 (I2C speed setup).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | total SCL period in input-clock ticks |
| `param_2` | `s32` | minimum SCL high time (ns) |
| `param_3` | `s32` | minimum SCL low time (ns) |
| `param_4` | `s32` | spike suppression/filter length in ticks |
| `param_5` | `u16` | input clock rate (MHz) used to convert ns to ticks |
| `param_6` | `ptr` | out: SCL high count (u16) |
| `param_7` | `ptr` | out: SCL low count (u16) |

**Notes:** Units of param_2/3/5 (ns and MHz) inferred from the divide-by-1000 rounding; register field names assume a DesignWare I2C core.

- Addresses by version: 219: 0x0C030368
- Called by: `ble_219_0c0458a6`
- Confidence: medium

## hal_i2c_check_tx_abort

**Check I2C raw error status and prepare the controller to recover from a TX abort**

param_1 is the I2C register base. Reads the raw interrupt status at +0x34; if none of bits 0,1,3,6 (0x4b: RX_UNDER, RX_OVER, TX_OVER, TX_ABRT) is set it returns 0. Otherwise reads TX_ABRT_SOURCE (+0x80); if bit 9 (SBYTE_NORSTRT, start byte sent while restart disabled) is set it sets IC_CON bit 5 (restart enable, reg +0), clears TAR bits 10 and 11 (reg +4, GC_OR_START/SPECIAL) and reads IC_CLR_TX_ABRT (+0x54) to clear the abort. Returns the abort source with bit 29 (0x20000000) added when RX_UNDER/RX_OVER/TX_OVER was flagged. Callers are 0x0c0302f4, 0x0c030ab0 and 0x0c030cb8.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | I2C controller register base |
| `param_2` | `u32` | unused (only echoed in the high word of the 64-bit decompiler return) |

**Returns** `u32`: 0 if no error, else TX_ABRT_SOURCE value with bit 29 marking FIFO over/under-run

**Notes:** Decompiler shows a 64-bit return; only the low word looks meaningful. Register names assume a Synopsys DesignWare I2C core.

- Addresses by version: 219: 0x0C0302B4
- Called by: `hal_i2c_irq_handler`, `hal_i2c_master_send_poll`, `hal_i2c_master_recv_poll`
- Confidence: medium

## hal_i2c_clear_busy

**Clear an I2C instance's bit in the busy mask DAT_2000a6c8; drop PM busy bit 2 when none remain**

Inside a BASEPRI critical section (BASEPRI raised to 0x40 when privileged; if it was not already 0x40 the call-site address 0x0c030276 and LR are logged to DAT_20003d70/DAT_20003d74, DAT_20003d70 reset to 0xffffffff on exit when BASEPRI was 0, BASEPRI restored afterwards) it clears bit param_1 of the byte mask DAT_2000a6c8 (one bit per I2C instance 0..5). When the mask becomes 0 it calls pm_busy_mask_clear_bit(2), so bit 2 of the global PM busy mask DAT_2000aa6c represents 'some I2C transfer in progress' and clearing it allows the system to sleep again. Called from hal_i2c_task_start_next (when no task is pending) and hal_i2c_close_internal.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | I2C instance 0..5 |

- Addresses by version: 219: 0x0C030268
- Called by: `hal_i2c_task_start_next`, `hal_i2c_close_internal`
- Calls: `pm_busy_mask_clear_bit`
- Confidence: high

## hal_i2c_close_internal

**Close an I2C instance: disable its NVIC IRQ and controller, clear busy, assert resets and gate clocks**

Returns immediately if the open flag DAT_2000a6f0[inst*0x70] is 0. Otherwise takes the IRQ number from the ROM record byte 0x0c081ac6[inst*12]; if it is < 0x4c (76) it disables the interrupt (NVIC ICER 0xe000e180 + 4*(irq>>5), DSB, ISB) and clears its pending bit (ICPR 0xe000e280). Clears IC_ENABLE (+0x6c) bit 0 of the register block from 0x0c081abc[inst*3], calls hal_i2c_clear_busy(inst), asserts the resets of the two CMU module ids stored at record bytes +9 and +8 (hal_cmu_reset_set), gates their clocks (hal_cmu_clock_disable) and clears the open flag. Called only through the exported wrapper 0x0c03133c, which asserts inst < 6. Reverse of the open path that enables clocks/releases resets.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | I2C instance 0..5 |

- Addresses by version: 219: 0x0C030A08
- Peripheral registers: `0xe000e180` (A), `0xe000e280` (A)
- Called by: `ble_219_0c03133c`
- Calls: `hal_i2c_clear_busy`, `hal_cmu_clock_disable`, `hal_cmu_reset_set`
- Confidence: high

## hal_i2c_master_recv_poll

**Polled I2C master read of n bytes, keeping the 8-deep FIFO filled with READ commands**

Same preamble as hal_i2c_master_send_poll: requires DAT_2000a6e4[inst*0x70] == 1 (else -0x80000000), and if IC_TAR (+4) != param_2 waits for the bus to be idle ((IC_STATUS +0x70) & 5 == 4, timeout 1000 units -> 0x8000000), disables the controller, reprograms the target (bit 15 -> 10-bit mode, TAR bit 12) and re-enables. It then spins IC_RXFLR (+0x78) iterations as a short delay and checks for a TX abort. Main loop until param_4 bytes were received: if IC_TXFLR (+0x74) + IC_RXFLR + 1 < 8 and commands remain, it pushes up to the free FIFO space of READ commands (IC_DATA_CMD +0x10 = 0x100, ORed with 0x400 RESTART on the first command when param_6 != 0 and 0x200 STOP on the last when param_7 != 0) while TFNF (status bit 1) is set; whenever RFNE (status bit 3) is set a byte is popped into param_3[received++] and the timeout base is reset, otherwise it checks for an abort (returned immediately) and a 1000-unit timeout (error 0x1000000), with an optional hal_sys_timer_delay_us(1) when param_8 != 0. If STOP was requested it finally waits for ACTIVITY (status bit 0) to clear (timeout 0x8000000). A last hal_i2c_check_tx_abort result is the return value (0 = success); *param_5 receives the byte count when non-NULL. Single caller hal_i2c_recv (read phase after the write).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | I2C instance 0..5 |
| `param_2` | `u32` | target address (bits 9:0), bit 15 = 10-bit addressing |
| `param_3` | `ptr` | receive buffer |
| `param_4` | `u32` | number of bytes to read |
| `param_5` | `ptr` | optional out: number of bytes received |
| `param_6` | `bool` | issue RESTART before the first read command |
| `param_7` | `bool` | issue STOP after the last read command |
| `param_8` | `bool` | insert a 1 us delay in every poll loop |

**Returns** `s32`: 0 ok; abort source; 0x8000000/0x1000000 timeouts; -0x80000000 not opened

**Notes:** If param_3 is NULL the received counter never advances (only the timeout ends the loop); decompiler artefact or latent bug.

- Addresses by version: 219: 0x0C030CB8
- Called by: `hal_i2c_recv`
- Calls: `hal_i2c_check_tx_abort`, `hal_sys_timer_delay_us`, `ble_ram_patch_thunk_2000031c`, `ble_ram_patch_thunk_20000570`
- Confidence: high

## hal_i2c_master_send_poll

**Polled I2C master write of n bytes with optional RESTART/STOP flags and timeouts**

Fails with -0x80000000 unless the instance state byte DAT_2000a6e4[inst*0x70] == 1 (opened). If IC_TAR (+4) differs from param_2 it first waits (timeout 1000 units converted to ticks by thunk 0x20000570, elapsed via thunk 0x2000031c) for IC_STATUS (+0x70) & 5 == 4 (TFE set, ACTIVITY clear), disables the controller (IC_ENABLE +0x6c bit 0), writes the new target (10-bit address field; param_2 bit 15 sets TAR bit 12 = 10-bit mode) and re-enables; a timeout returns 0x8000000 with 0 bytes sent. After a hal_i2c_check_tx_abort it writes each byte to IC_DATA_CMD (+0x10): the first byte carries 0x400 (RESTART) when param_6 != 0 and the last byte 0x200 (STOP) when param_7 != 0; before each write it waits for TFNF (status bit 1) with abort checks (any abort source is returned immediately) and a 1000-unit timeout (error 0x4000000). Afterwards it waits for TFE (status bit 2, error 0x2000000) when no STOP was requested, else for the bus to go idle ((status & 5) == 4, error 0x8000000). Whenever param_8 != 0 each polling iteration also calls hal_sys_timer_delay_us(1). The number of bytes written is stored to *param_5 when non-NULL. Returns 0 on success, otherwise the TX_ABRT_SOURCE value from hal_i2c_check_tx_abort or one of the timeout codes above. Callers: hal_i2c_send and hal_i2c_recv (write phase).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | I2C instance 0..5 |
| `param_2` | `u32` | target address (bits 9:0), bit 15 = 10-bit addressing |
| `param_3` | `ptr` | bytes to transmit |
| `param_4` | `s32` | number of bytes |
| `param_5` | `ptr` | optional out: number of bytes actually written |
| `param_6` | `bool` | issue RESTART before the first byte |
| `param_7` | `bool` | issue STOP after the last byte |
| `param_8` | `bool` | insert a 1 us delay in every poll loop |

**Returns** `s32`: 0 ok; abort source; 0x8000000/0x4000000/0x2000000 timeouts; -0x80000000 not opened

**Notes:** The timeout unit of thunk 0x20000570 (ms or us -> ticks) is not confirmed.

- Addresses by version: 219: 0x0C030AB0
- Called by: `hal_i2c_send`, `hal_i2c_recv`
- Calls: `hal_i2c_check_tx_abort`, `hal_sys_timer_delay_us`, `ble_ram_patch_thunk_2000031c`, `ble_ram_patch_thunk_20000570`
- Confidence: high

## hal_i2c_recv

**Exported I2C write-then-read: send the register/command bytes, then read rx_len bytes with RESTART+STOP**

Asserts param_1 < 6 (infinite loop otherwise). Calls hal_i2c_master_send_poll with the caller's arguments (instance, address, tx buffer, tx length, and the flags it was given; the decompiler drops them); if that returns non-zero the error is returned (via the caller's register) and nothing is read. Otherwise calls hal_i2c_master_recv_poll(inst, param_2, param_5, param_6, NULL, restart = 1, stop = 1, delay = 0), i.e. a repeated-START read of param_6 bytes into param_5 followed by STOP. This is the usual register-read transaction (write register index, restart, read). Caller 0x0c045940 (device-driver read entry) passes (inst, p[0] address, p+4 tx pointer, p[1] tx length, p+8 rx pointer, p[2] rx length) and returns the rx length on success.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | I2C instance 0..5 (asserted) |
| `param_2` | `u32` | target address (bit 15 = 10-bit) |
| `param_3` | `ptr` | bytes to write first |
| `param_4` | `u32` | number of bytes to write |
| `param_5` | `ptr` | receive buffer |
| `param_6` | `u16` | number of bytes to read |

**Notes:** Decompiler lost the argument forwarding to the send phase; the flags used for the write phase (restart/stop) are therefore not visible.

- Addresses by version: 219: 0x0C03136C
- Called by: `ble_219_0c045940`
- Calls: `hal_i2c_master_send_poll`, `hal_i2c_master_recv_poll`
- Confidence: medium

## hal_i2c_send

**Exported I2C write: assert instance < 6 and tail-call hal_i2c_master_send_poll with all arguments**

Validates param_1 (instance) < 6, hanging in an assert loop otherwise, then tail-calls hal_i2c_master_send_poll with the unchanged register/stack arguments (instance, target address, tx buffer, length, out-count pointer, restart flag, stop flag, delay flag); its result is returned unchanged. The decompiler shows the call without arguments because they are passed through untouched. Caller 0x0c0458e4 (a device-driver write entry) uses it as write(fd, addr = buf[0], data = buf+1, len-1).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | I2C instance 0..5 (asserted) |

**Returns** `s32`: result of hal_i2c_master_send_poll (0 ok, error/abort code)

**Notes:** Remaining parameters are identical to hal_i2c_master_send_poll.

- Addresses by version: 219: 0x0C03134C
- Called by: `ble_219_0c0458e4`
- Calls: `hal_i2c_master_send_poll`
- Confidence: high

## hal_i2c_task_done_handler

**I2C completion handler: invoke the callback of the finished task and advance the 2-entry task ring**

param_1 is the I2C instance (0/1; per-instance state stride 0x70, registers from table 0x0c081abc). Uses a 2-entry ring of 0x30-byte task slots indexed by DAT_2000a6f2[inst]. If the current slot has the stop flag (DAT_2000a708) or a non-zero DAT_2000a71c, it clears the controller's interrupt-mask register (+0x30) and clears the enable bit of IC_ENABLE (+0x6c bit 0). If bit 0 of the slot flag byte (DAT_2000a6e5) is set it only marks the next slot ready (DAT_2000a6e4 = 1); otherwise it calls the slot's callback (DAT_2000a720) with (inst, next buffer pointer, 3 stored fields and two products of the 16-bit fields at +0x18/+0x1a/+0x1c). Finally it decrements the pending-task count DAT_2000a6f3 (infinite-loop assert if already 0) and toggles the ring index. No direct callers (called from the I2C ISR path).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | I2C instance index (0 or 1) |

**Notes:** Register identification (DesignWare-style I2C: +0x30 INTR_MASK, +0x6c ENABLE) is solid; the exact slot/task field meanings and callback signature are inferred.

- Addresses by version: 219: 0x0C030198
- Confidence: low

## hal_i2c_task_start_next

**Kick the next queued interrupt-mode I2C task of an instance: program TAR/thresholds, unmask IRQs, enable**

param_1 is the I2C instance (per-instance state stride 0x70 from 0x2000a6e4, register base from the ROM table 0x0c081abc[inst*3]). If the pending-task count DAT_2000a6f3[inst] is 0: resets it, copies the next-slot index DAT_2000a6f1 into the current index DAT_2000a6f2, sets DAT_2000a6f0[inst] = 1 and calls hal_i2c_clear_busy(inst) (drops the PM busy bit when all instances are idle), then returns. Otherwise the current slot index must be < 2 (assert loop); slot = inst*0x70 + idx*0x30. If the slot's buffer word DAT_2000a6f4[slot] is 0 the flag byte DAT_2000a6e5[inst] bit 2 must be clear (assert), else IC_RX_TL (+0x3c) = 2; if the task type byte DAT_2000a710[slot] == 2, IC_TX_TL (+0x38) = 5; IC_INTR_MASK (+0x30) = 0xaff (all sources except ACTIVITY and START_DET). If IC_ENABLE_STATUS (+0x9c) bit 0 shows the controller disabled: set IC_CON (+0) bit 5 (RESTART_EN); if flag bit 2 is set program IC_TAR (+4) from the 16-bit address field DAT_2000a70a[slot] (low 10 bits, bit 15 selects 10-bit addressing -> TAR bit 12); then set IC_ENABLE (+0x6c) bit 0. No direct callers (reached from the I2C ISR callback / task submission path); pairs with hal_i2c_task_done_handler which advances the 2-entry task ring.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | I2C instance 0..5 |

**Notes:** Register names assume a Synopsys DesignWare I2C core; slot field meanings (type byte 2, flag bit 2 = 'address from slot') are inferred.

- Addresses by version: 219: 0x0C030428
- Calls: `hal_i2c_clear_busy`
- Confidence: medium

## hal_init_stub_ret0_a

**Stub returning 0, called from the platform init routine**

Returns 0 and does nothing. It is called from 0x0c03ab80 in the same sequence as hal_cache_enable and its twin stub at 0x0c02ed28, apparently placeholder init steps (e.g. unused cache/feature setup) whose result is not checked.

**Returns** `u32`: always 0

**Notes:** Original purpose unknown (empty implementation in this build).

- Addresses by version: 219: 0x0C02ED24
- Called by: `ble_219_0c03ab80`
- Confidence: medium

## hal_init_stub_ret0_b

**Second stub returning 0, called from the platform init routine**

Returns 0 and does nothing; twin of hal_init_stub_ret0_a (0x0c02ed24). Called only from 0x0c03ab80.

**Returns** `u32`: always 0

**Notes:** Original purpose unknown (empty implementation in this build).

- Addresses by version: 219: 0x0C02ED28
- Called by: `ble_219_0c03ab80`
- Confidence: medium

## hal_irq_get_handler_table

**Return the base address of the RAM handler table at 0x2000aa80**

Returns the constant pointer 0x2000aa80, the table of 4-byte ISR entry addresses that the UART install routine (0x0c033d94) fills. Single caller 0x0c0467b8.

**Returns** `ptr`: address 0x2000aa80

- Addresses by version: 219: 0x0C0342B8
- Called by: `ble_219_0c0467b8`
- Confidence: medium

## hal_periph_9000_set_field_10_7

**Set a 4-bit field (bits 10:7) in the register at 0x40009004**

Read-modify-write of 0x40009004: clears bits 10:7 (mask 0xfffff87f) and ORs in param_1 << 7. Values >= 15 are rejected by spinning forever (assert-style trap). Called three times from the 0x0c0401b0-0x0c040378 group; the register block at 0x40009000 is BES-specific and undocumented, the field looks like a divider/selector index 0..14.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | field value, must be < 15 |

**Notes:** Peripheral identity of 0x40009000 is unknown; the divider/selector interpretation is a guess.

- Addresses by version: 219: 0x0C0326A8
- Peripheral registers: `0x40009004` (RW)
- Called by: `hal_analogif_reg_read`, `hal_analogif_reg_write`, `ble_219_0c040378`
- Confidence: low

## hal_pmu_get_saved_status_nibble

**Return the status nibble saved from register 0x40080038**

Returns the byte DAT_20003ce4, which hal_pmu_save_and_clear_status_nibble (0x0c02ece4) filled with the low 4 bits of register 0x40080038 at boot. The chip-init routine 0x0c03a038 tests bit 0 and bit 1 of it to choose DAT_20003d6c (2 when bit0, 4 when bit1, otherwise a value derived from a PMU register read), so it behaves like a reset/boot-cause indicator.

**Returns** `u8`: saved low nibble of 0x40080038

**Notes:** Semantics (reset cause vs wake source) inferred from how 0x0c03a038 uses it.

- Addresses by version: 219: 0x0C02ECD8
- Called by: `ble_219_0c03a038`
- Confidence: medium

## hal_pmu_save_and_clear_status_nibble

**Save low 4 bits of reg 0x40080038 to DAT_20003ce4 and write 1s back to them**

Reads 0x40080038, stores (value & 0xf) in DAT_20003ce4, then reads the register again and writes value | 0xf back. Setting the nibble with a read-modify-write is consistent with write-1-to-clear status bits, so this captures and acknowledges the boot/reset-cause flags. Called early from the platform init routine 0x0c03ab80.

**Notes:** 0x40080038 is an undocumented BES register; write-1-to-clear behaviour is an assumption.

- Addresses by version: 219: 0x0C02ECE4
- Peripheral registers: `0x40080038` (RW)
- Called by: `ble_219_0c03ab80`
- Confidence: medium

## hal_sys_timer_alarm_elapsed

**Ticks elapsed on the free-running counter since the alarm was armed**

Computes -(counter + DAT_20003c10), where counter is the register at 0x40002004 and DAT_20003c10 holds the negated counter value stored when the alarm was started, i.e. start_value - current_value, giving elapsed ticks of a down-counting timer.

**Returns** `s32`: elapsed ticks since alarm start

- Addresses by version: 219: 0x0C0330FC
- Peripheral registers: `0x40002004` (R)
- Called by: `hwtimer_handler`, `hwtimer_stop`
- Confidence: medium

## hal_sys_timer_alarm_get_count

**Read the alarm timer current-value register**

Returns the raw 32-bit value of register 0x40002024 (current/remaining count of the alarm timer whose load register is 0x40002020).

**Returns** `u32`: raw timer count

- Addresses by version: 219: 0x0C0330F0
- Peripheral registers: `0x40002024` (R)
- Called by: `hwtimer_start_internal`, `hwtimer_stop`
- Confidence: medium

## hal_sys_timer_alarm_is_running

**Return whether the alarm timer enable bit is set**

Reads control register 0x40002028 and returns bit7 (value 0 or 1), the enable flag that the alarm start routine sets and the stop routine clears.

**Returns** `u32`: 1 if the alarm is armed, else 0

- Addresses by version: 219: 0x0C0330E0
- Peripheral registers: `0x40002028` (R)
- Called by: `hwtimer_handler`
- Confidence: medium

## hal_sys_timer_alarm_start

**Arm the 0x4000200x timer for a one-shot wake after param_1 ticks**

Clamps the tick count: values 0 and 1 become 1, larger values become param_1 - 1. Saves the negated current counter (0x40002004) into DAT_20003c10 as the reference for later elapsed-time reads, writes the clamped value to the load register 0x40002020 and sets bit7 (enable) in the control register 0x40002028. Counterparts: stop at 0x0c0330b8, elapsed at 0x0c0330fc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | timer ticks until the alarm fires |

- Addresses by version: 219: 0x0C03308C
- Peripheral registers: `0x40002004` (R), `0x40002020` (W), `0x40002028` (RW)
- Called by: `hwtimer_handler`, `hwtimer_start_internal`, `hwtimer_stop`
- Confidence: medium

## hal_sys_timer_alarm_stop

**Stop the alarm timer and clear its pending interrupt**

Clears bit7 (enable) in 0x40002028, writes 1 to 0x4000202c (interrupt acknowledge) and writes 0x2000 to NVIC ICPR0 (0xe000e280), clearing the pending state of IRQ 13. Complements the alarm start at 0x0c03308c.

- Addresses by version: 219: 0x0C0330B8
- Peripheral registers: `0x40002028` (RW), `0x4000202c` (W), `0xe000e280` (W)
- Called by: `hwtimer_handler`, `hwtimer_start_internal`, `hwtimer_stop`
- Confidence: medium

## hal_sys_timer_calc_loop_ticks

**Measure timer ticks taken by a busy loop of N iterations, optionally the DWT cycle cost of a timer read**

Calibration helper. If param_2 is non-NULL it first calls FUN_0c089478 (thunk to 0x0c03aafc, e.g. a DWT/trace-enable check or interrupt lock), resets DWT_CYCCNT (0xE0001004) to 0, sets CYCCNTENA (bit 0 of DWT_CTRL 0xE0001000), performs one read of the hardware timer value register 0x40003004, reads CYCCNT back, clears CYCCNTENA and stores the measured cycle count in *param_2; FUN_0c089488 (thunk to 0x0c03ab18) is called when the first call returned 0 (restore). Then it waits for the timer register to change (edge alignment), spins a countdown loop of param_1 iterations and returns the difference between the timer value after the edge and after the loop (the timer counts down, so the result is positive ticks elapsed). Used to calibrate software delay loops / CPU frequency against the system timer.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | number of busy-loop iterations to time |
| `param_2` | `ptr` | optional u32 * receiving DWT cycles spent on one timer read |

**Returns** `s32`: timer ticks elapsed during the loop

**Notes:** 0x40003004 is the BES system timer current-value register (down-counter), as also used by norflash_delay_us.

- Addresses by version: 219: 0x0C086754
- Peripheral registers: `0x40003004` (R), `0xe0001000` (ARW), `0xe0001004` (RW)
- Calls: `ble_thunk_call_0c03aafc`, `ble_thunk_call_0c03ab18`
- Confidence: medium

## hal_sys_timer_delay_us

**Busy-wait for param_1 microseconds on the hardware tick counter**

Converts param_1 to float, computes ticks = (us / 1000.0) * DAT_20003548 + 0.99 where DAT_20003548 holds ticks per millisecond, then samples the free-running counter at 0x40002004 and spins until (start - now) is no longer below the tick count (counter counts downward / difference taken unsigned). Negative or zero tick counts return immediately. Always returns 0. Callers are the BLE controller code at 0x0c030ab0/0x0c030cb8 and the delay at 0x0c033328.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | delay in microseconds |

**Returns** `u32`: always 0

**Notes:** Direction of the counter at 0x40002004 is inferred from the (start - now) comparison.

- Addresses by version: 219: 0x0C033030
- Peripheral registers: `0x40002004` (R)
- Called by: `hal_i2c_master_send_poll`, `hal_i2c_master_recv_poll`, `ble_219_0c033328`, `ble_219_0c037a7c`
- Confidence: medium

## hal_sysipc_close

**Release one user of an IPC channel and shut the channel down when unused**

param_1 is the channel (0 or 1; otherwise returns 1), param_2 the per-channel user/type bit. Clears the user bit in the mask DAT_2000a990[ch] and zeroes the user's slot in the callback arrays at 0x2000a9bc and 0x2000aa54. When the mask becomes 0 it disables both NVIC interrupt lines taken from the tables 0x0c083e1c and 0x0c0857ec (writes to ICER, 0xe000e180 area, followed by DSB/ISB), writes the channel's clear bits (0x2000 then 0x8000 for ch0; 0x4000 then 0x10000 for ch1) to register 0x400000a4, and resets the queue heads and state (0x2000aa4c, 0x2000a9cc, 0x2000a9a8, 0x2000a998). Returns 0 on success.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | IPC channel index (0 or 1) |
| `param_2` | `u32` | user/message-type bit index (0 or 1) |

**Returns** `u32`: 0 on success, 1 for an invalid channel

**Notes:** Identification as the BES inter-core IPC (hal_sysipc) is inferred from the TX-queue/mailbox pattern with registers 0x400000a0 (set) / 0x400000a4 (clear); register semantics unverified.

- Addresses by version: 219: 0x0C03171C
- Peripheral registers: `0x400000a4` (W), `0xe000e100` (A)
- Called by: `ble_219_0c03bb70`, `ble_219_0c04542c`
- Confidence: low

## hal_sysipc_rx_irq_disable

**Disable the NVIC interrupt of an IPC channel**

Returns 1 if param_1 > 1. Otherwise looks up the IRQ number in the signed byte table at 0x0c083e1c[param_1] and, if it is non-negative, writes 1 << (irq & 31) to the NVIC ICER word (0xe000e180 + 4*(irq>>5)) followed by DSB and ISB. Returns 0. Called from 0x0c03bfbc.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | IPC channel index (0 or 1) |

**Returns** `u32`: 0 on success, 1 if the channel is invalid

**Notes:** Same IPC-module identification caveat as hal_sysipc_close.

- Addresses by version: 219: 0x0C031848
- Peripheral registers: `0xe000e100` (A)
- Called by: `ble_219_0c03bfbc`
- Confidence: low

## hal_sysipc_rx_irq_setup

**Enable the IPC channel interrupt and (channel 1) install its vector and priority**

Stores param_2 in DAT_2000a984, then enables the NVIC interrupt number from the byte table 0x0c083e1c[param_1] (write to ISER). For param_1 == 1 additionally writes 10 to register 0x400000a4, reads VTOR (0xe000ed08) and stores the handler address 0x0c0314bc at vector offset 0xcc (IRQ 35), issues a DSB, sets that interrupt's priority byte (0xe000e423) to 0xa0 and writes 0x4000 to 0x400000a0. Returns 0. Called from 0x0c03bb70, which also calls hal_sysipc_close.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `s32` | IPC channel index |
| `param_2` | `u32` | value saved in DAT_2000a984 (callback or context) |

**Returns** `u32`: always 0

**Notes:** Purpose of the DAT_2000a984 value and of the 0x400000a0/a4 bit patterns is not confirmed.

- Addresses by version: 219: 0x0C031978
- Peripheral registers: `0x400000a0` (W), `0x400000a4` (W), `0xe000e100` (A), `0xe000e423` (W), `0xe000ed08` (R)
- Called by: `ble_219_0c03bb70`
- Confidence: low

## hal_sysipc_send

**Queue a two-word IPC message on channel 0/1 for user type 0/1 and ring the doorbell (0x400000a0)**

Returns 1 if param_1 (channel) > 1, 2 if param_2 (user/type) > 1, 3 if bit type of the open mask DAT_2000a990[ch] is clear. Inside a BASEPRI critical section (BASEPRI 0x40; call site 0x0c0318ae and LR logged to DAT_20003d70/DAT_20003d74 when not already at 0x40, DAT_20003d70 reset to 0xffffffff on exit when it was 0) it picks the first free of three 0x14-byte message slots of the channel at 0x2000a9d4 + ch*0x3c (in-use bytes at +0x10: 0x2000a9e4, 0x2000a9f8, 0x2000aa0c); if all are busy returns 0xffffffff. The slot is filled: next = 0, type byte = param_2, +8 = param_4, +0xc = param_3, in-use = 1. If the active list head DAT_2000a9cc[ch] is empty the slot becomes the head and the doorbell is rung by writing 4 (ch0) or 8 (ch1) to 0x400000a0 (read back); otherwise the slot is appended to the pending list DAT_2000aa4c[ch]. If the channel busy byte DAT_2000a98c[ch] was 0 it is set, and if the global flag DAT_2000a988 was 0 it calls pm_busy_mask_set_bit(0) and sets DAT_2000a988 (veto sleep while IPC traffic is in flight). Returns 0 on success. Callers: 0x0c03ac98 (controller/host message path), 0x0c03eb84, 0x0c0454d0 (HCI send: 'error hci send : length = %d'). Completion is handled by hal_sysipc_tx_done_irq_handler.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | IPC channel 0 or 1 |
| `param_2` | `u32` | user/message type 0 or 1 (selects the tx-done callback) |
| `param_3` | `u32` | first payload word (stored at node+0xc, passed first to the callback) |
| `param_4` | `u32` | second payload word (stored at node+8, e.g. length) |

**Returns** `s32`: 0 ok; 1 bad channel; 2 bad type; 3 not opened; -1 no free message slot

**Notes:** Which of param_3/param_4 is the data pointer vs length is not verified; the IPC identification follows wave 1.

- Addresses by version: 219: 0x0C031884
- Peripheral registers: `0x400000a0` (RW)
- Called by: `ble_219_0c03ac98`, `bt_drv_intersys_send_saved_iface`, `ble_219_0c0454d0`
- Calls: `pm_busy_mask_set_bit`
- Confidence: medium

## hal_trace_buf_putc

**Append a byte to a line buffer and flush through a write callback when full**

param_1 points to an output-stream object: write callback at +0x50, capacity (u16) at +0x54, fill count (u16) at +0x56, buffer pointer at +0x58. If room remains, stores param_2 at buffer[fill++]; returns 0 if still not full. When the buffer is full (or already was) and non-empty, repeatedly calls the callback with the buffer (the decompiler shows only the buffer pointer as argument, the length presumably in r1), advancing by the number of bytes consumed and decreasing the fill count, until the buffer is empty; a negative callback result is returned immediately. Returns the total bytes flushed.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | output stream object (callback +0x50, capacity +0x54, count +0x56, buffer +0x58) |
| `param_2` | `u8` | byte to append |

**Returns** `s32`: 0 if only buffered, bytes flushed on flush, or negative error from the callback

**Notes:** Three callers at 0x0c0356dc, 0x0c0357b8 and 0x0c035900 (print formatting path).

- Addresses by version: 219: 0x0C035684
- Called by: `trace_fmt_unsigned`, `trace_fmt_signed`, `ble_219_0c035900`
- Confidence: medium

## hal_trace_get_state_vars

**Copy three global words (0x2000baac, baa8, baa4) to caller-provided pointers**

If param_1 and param_2 are both non-NULL, stores DAT_2000baac to *param_1, DAT_2000baa8 to *param_2 and DAT_2000baa4 to *param_3 (param_3 is not NULL-checked); otherwise does nothing. No direct callers - reached indirectly.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | receives DAT_2000baac |
| `param_2` | `ptr` | receives DAT_2000baa8 |
| `param_3` | `ptr` | receives DAT_2000baa4 (the flag set by 0x0c036388) |

**Notes:** Semantics of the three values unknown.

- Addresses by version: 219: 0x0C0363A4
- Confidence: low

## hal_trace_set_flag_baa4

**Set the global flag at 0x2000baa4 to 1**

Writes 1 into DAT_2000baa4 and returns. No direct callers - invoked through a function pointer/hook. The flag is later copied out by the accessor at 0x0c0363a4.

**Notes:** Role of the flag is unknown; it sits next to the crash/trace RAM variables (0x2000b9xx..baxx) so it may be a crash/trace state indicator.

- Addresses by version: 219: 0x0C036388
- Confidence: low

## hwtimer_handler

**Sys-timer alarm ISR of the hwtimer list: expire due timers, re-arm the alarm and run callbacks**

Interrupt handler of the BES hwtimer list module (static timer pool 0x2000C5F4..0x2000C720, 20-byte nodes: state +0, next +4, ticks +8 (delta to predecessor, head = armed value), handler +0xC, param +0x10; states 1 = allocated/idle, 2 = active, 3 = expired, 4 = in callback). Runs under BASEPRI 0x40 with the DAT_20003D70/74 lock trace. If the active list head DAT_2000C724 is NULL it counts a spurious interrupt in DAT_2000C5E8 and traps (infinite loop) if hal_sys_timer_alarm_is_running() is still set. Otherwise reads hal_sys_timer_alarm_elapsed(); if elapsed+1 < head->ticks the alarm fired early: DAT_2000C5EC++ and trap if the alarm is not running. Else over = elapsed - head->ticks (0 if not past), marks the head expired (3) and walks the list: nodes whose delta <= over are also marked expired and consume it; the first node with delta > over becomes the new head with delta reduced by over and hal_sys_timer_alarm_start(delta) re-arms; if none remains the active list becomes NULL and hal_sys_timer_alarm_stop() is called. The expired chain is moved to DAT_2000C728 and processed in order: node state = 4, next = NULL, and if a handler is set BASEPRI is restored, handler(param) is called, the lock is re-taken and, if the node is still in state 4 (not restarted/stopped by the callback), it returns to state 1. Siblings: hwtimer_start_internal (0x0c04200c), hwtimer_start (0x0c042170), hwtimer_stop (0x0c04219c). No direct caller: registered with the sys-timer alarm interrupt.

**Notes:** Matches BES hwtimer_list.c (hwtimer_handler). DAT_2000C5E8/EC look like the module's spurious/early-interrupt counters.

- Addresses by version: 219: 0x0C041ED4
- Calls: `hal_sys_timer_alarm_start`, `hal_sys_timer_alarm_stop`, `hal_sys_timer_alarm_is_running`, `hal_sys_timer_alarm_elapsed`
- Confidence: high

## hwtimer_start

**Validate a hwtimer id against the static pool and start it with the given tick timeout**

Accepts only pointers inside the timer pool 0x2000C5F4..0x2000C70C (15 nodes of 20 bytes); any other id returns 2 (invalid id). Valid ids are forwarded to hwtimer_start_internal(id, 0, NULL, NULL, ticks) (0x0c04200c), so the handler/param stored in the node are kept. Returns that call's status (0 ok, 3 wrong state). Called from 0x0c03ac44, which also uses hwtimer_stop. BES hwtimer_list.c API.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hwtimer id (node pointer inside 0x2000C5F4..0x2000C70C) |
| `param_2` | `u32` | timeout in sys-timer ticks |

**Returns** `u32`: 0 ok, 2 invalid id, 3 timer not startable

- Addresses by version: 219: 0x0C042170
- Called by: `ble_219_0c03ac44`
- Calls: `hwtimer_start_internal`
- Confidence: high

## hwtimer_start_internal

**Insert a hwtimer into the delta-sorted active list and (re)arm the sys-timer alarm (BES __hwtimer_start)**

Under BASEPRI 0x40 (DAT_20003D70/74 lock trace) requires the node to be in state 1 (allocated) or 4 (in callback), otherwise returns 3. Sets state 2 (active); if param_2 is non-zero it also updates handler (+0xC) and param (+0x10) from param_3/param_4. A timeout of 0 becomes 1 tick. If the active list DAT_2000C724 is empty the node becomes head with next = NULL and hal_sys_timer_alarm_start(ticks) arms the alarm. Otherwise it reads the remaining count of the running alarm via hal_sys_timer_alarm_get_count() and traps (infinite loop) if it exceeds the head's delta (and is > 1). If the new timeout is shorter than the remaining count the node becomes the new head (head delta = remaining - timeout, alarm stopped and restarted with the new timeout); else timeout -= remaining and the list is walked, subtracting each predecessor's delta until a node with delta >= timeout is found, whose delta is reduced by timeout, and the node is linked in before it (or at the tail). The node's ticks field receives its final delta. Returns 0. Called by hwtimer_start (0x0c042170) with update = 0 and presumably by hwtimer_update_then_start with update = 1. Group: hwtimer_handler (0x0c041ed4), hwtimer_stop (0x0c04219c).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hwtimer node (20 bytes: state, next, ticks, handler, param) |
| `param_2` | `s32` | non-zero: also store the new handler/param |
| `param_3` | `ptr` | callback handler(param) stored at +0xC when param_2 != 0 |
| `param_4` | `ptr` | callback argument stored at +0x10 when param_2 != 0 |
| `param_5` | `u32` | timeout in sys-timer ticks (0 is treated as 1) |

**Returns** `u32`: 0 on success, 3 if the timer is not in state 1 or 4

**Notes:** Matches BES hwtimer_list.c __hwtimer_start(id, update, handler, param, ticks).

- Addresses by version: 219: 0x0C04200C
- Called by: `hwtimer_start`
- Calls: `hal_sys_timer_alarm_start`, `hal_sys_timer_alarm_stop`, `hal_sys_timer_alarm_get_count`
- Confidence: high

## hwtimer_stop

**Remove a hwtimer from the active or expired list, fixing deltas and re-arming the alarm**

Returns 2 for ids outside the pool 0x2000C5F4..0x2000C70C. Under BASEPRI 0x40 (DAT_20003D70/74 lock trace) acts on the node state: 1 (idle) -> returns 0 unchanged; 4 (callback running) -> returns 4; other unknown states -> 3. State 2 (active): if the node is not the head DAT_2000C724 it is searched in the list, unlinked and its delta is added to its successor (not found -> trap loop). If it is the head: reads hal_sys_timer_alarm_get_count() (trap if larger than head delta and > 1), hal_sys_timer_alarm_stop(), and if a successor exists either adds the remaining count to the successor's delta (count > 0) or, when the alarm already expired (count == 0), computes over = hal_sys_timer_alarm_elapsed() - head delta (trap if elapsed+1 < delta) and subtracts it along the list, zeroing deltas that are fully consumed; then hal_sys_timer_alarm_start(successor delta) and the successor becomes head. State 3 (expired, in DAT_2000C728 list): unlinked from the expired list (head or searched; not found -> trap). In all handled cases the node ends in state 1 with next = NULL and 0 is returned. Group: hwtimer_handler (0x0c041ed4), hwtimer_start (0x0c042170), hwtimer_start_internal (0x0c04200c). Called from 0x0c03ac44.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | hwtimer id (node pointer inside the static pool) |

**Returns** `u8`: 0 stopped/idle, 2 invalid id, 3 bad state, 4 timer is executing its callback

**Notes:** Matches BES hwtimer_list.c hwtimer_stop.

- Addresses by version: 219: 0x0C04219C
- Called by: `ble_219_0c03ac44`
- Calls: `hal_sys_timer_alarm_start`, `hal_sys_timer_alarm_stop`, `hal_sys_timer_alarm_get_count`, `hal_sys_timer_alarm_elapsed`
- Confidence: high

## norflaship_cfg38_clear_bit12

**Clear bit 12 of register REG_038**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). REG_038 &= ~0x1000.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C0879C0
- Called by: `norflash_set_burst_wrap`
- Confidence: low

## norflaship_cfg38_set_bit0

**Set bit 0 of register REG_038**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). REG_038 |= 1; probably an enable bit of the cached/memory-mapped access path.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C0879D4
- Called by: `norflash_set_burst_wrap`
- Confidence: low

## norflaship_cfg38_set_bit12

**Set bit 12 of register REG_038**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). REG_038 |= 0x1000. Counterpart of norflaship_cfg38_clear_bit12.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C0879AC
- Called by: `norflash_set_burst_wrap`
- Confidence: low

## norflaship_clear_fifos

**Reset both TX and RX FIFOs of the flash IP**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle, writes 3 to REG_018 (bit0 = clear RX FIFO, bit1 = clear TX FIFO), then waits for idle again.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

**Notes:** Bit assignment of REG_018 inferred from the 1/2/3 trio of helpers.

- Addresses by version: 219: 0x0C0877E4
- Called by: `norflash_status_s0_s7`, `norflash_status_s8_s15`, `norflash_wait_busy_or_suspend`, `norflash_reset`, `norflash_write_reg`, `norflash_read_jedec_id`, `norflash_sample_delay_calib`
- Confidence: medium

## norflaship_clear_rxfifo

**Reset the RX FIFO of the flash IP**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle, writes 1 to REG_018, waits for idle again. Called before read operations to discard stale data.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C087800
- Called by: `norflash_set_continuous_read`, `norflash_reset`, `norflash_sample_delay_calib`
- Confidence: medium

## norflaship_clear_txfifo

**Reset the TX FIFO of the flash IP**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle, writes 2 to REG_018, waits for idle again. Called before write/program operations.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C08781C
- Called by: `norflash_set_burst_wrap`, `norflash_write_reg`, `norflash_page_program`
- Confidence: medium

## norflaship_ctrl_clear_bit0

**Wait for idle, then clear bit 0 of REG_004**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Spins while REG_00C bit0 (busy) is set, then REG_004 &= ~1. Ends the data-phase/extended mode selected by norflaship_send_cmd_word.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C087774
- Called by: `norflash_restore_read_config`, `norflash_reset`, `norflash_set_read_mode`, `norflash_post_operation`, `norflash_post_operation_alt`, `norflash_erase`, `norflash_page_program`
- Confidence: medium

## norflaship_ctrl_clear_bit25

**Clear bit 25 of flash-IP control register REG_004 after waiting for idle**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits until REG_00C bit0 (busy) clears, then REG_004 &= 0xFDFFFFFF. Counterpart of norflaship_ctrl_set_bit25; bit meaning not documented (probably a read/receive-phase enable).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C0875C8
- Called by: `norflash_set_continuous_read`, `norflash_reset`
- Confidence: medium

## norflaship_ctrl_set_bit25

**Set bit 25 of flash-IP control register REG_004 after waiting for idle**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits until REG_00C bit0 (busy) clears, then REG_004 |= 0x02000000. Counterpart of norflaship_ctrl_clear_bit25; bit meaning not documented (probably a read/receive-phase enable).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C0875E4
- Called by: `norflash_set_continuous_read`, `norflash_restore_read_config`, `norflash_set_read_mode`, `norflash_post_operation`, `norflash_post_operation_alt`
- Confidence: medium

## norflaship_fill_txfifo

**Push up to FIFO-space bytes from a buffer into the TX FIFO**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Same copy loop as norflaship_set_len_and_fill_txfifo but without touching the length field. Reads REG_00C[12:8]; if 0 returns param_3; otherwise writes min(count, param_3) bytes from param_2 to REG_008 one at a time and returns the remaining byte count (0 if everything was written). Called from the flash program loop (0x0c089064).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `ptr` | source byte buffer |
| `param_3` | `s32` | number of bytes to send |

**Returns** `s32`: bytes remaining to send, 0 when all written

- Addresses by version: 219: 0x0C08765C
- Called by: `norflash_page_program`
- Confidence: medium

## norflaship_get_cfg14_byte2

**Read bits 16..23 of config register REG_014**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Returns (REG_014 & 0xFFFFFF) >> 16. Used by the routine at 0x0c088bb8 to save the setting before temporarily changing it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

**Returns** `u8`: REG_014[23:16]

- Addresses by version: 219: 0x0C08785C
- Called by: `norflash_sample_delay_calib`
- Confidence: low

## norflaship_read_rxfifo_byte

**Read the low byte of flash-IP register REG_010 (RX data)**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Returns REG_010 & 0xFF; this is the receive FIFO / read-data register where bytes returned by the flash chip (ID, status, data) are fetched. Callers are the read-ID / read-status / read-data routines.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

**Returns** `u8`: received byte (0..255)

- Addresses by version: 219: 0x0C0876A0
- Called by: `norflash_status_s0_s7`, `norflash_status_s8_s15`, `norflash_wait_busy_or_suspend`, `norflash_write_reg`, `norflash_read_jedec_id`, `norflash_sample_delay_calib`
- Confidence: medium

## norflaship_send_cmd_byte

**Issue a command opcode with one operand byte (REG_004 bit0 cleared)**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for busy (REG_00C bit0) to clear, clears REG_004 bit0, then writes REG_000 = param_2 | (param_3 << 8), which starts the transaction. Used for simple flash commands such as write-enable or status-register writes where no 24-bit address follows.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | command opcode (low byte) |
| `param_3` | `u32` | operand/data byte or bytes placed in REG_000[15:8] |

- Addresses by version: 219: 0x0C0876D4
- Called by: `norflash_set_continuous_read`, `norflash_set_burst_wrap`, `norflash_reset`, `norflash_write_reg`, `norflash_erase`, `norflash_page_program`
- Confidence: medium

## norflaship_send_cmd_ext

**Start a transaction with command, data length and extended field**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle, sets REG_004 length field to param_3 & 0x1FFF and bit0, then writes REG_000 = ((param_4 & 0x3FFF) << 13) | param_2 | 0x100. The 0x100 bit and the 14-bit field at bit 13 look like a flag plus an address/operand; used by read and program paths together with the FIFO helpers.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | command opcode / low bits of REG_000 |
| `param_3` | `u32` | data phase length in bytes (13-bit) |
| `param_4` | `u32` | 14-bit operand (e.g. address bits) placed at REG_000[26:13] |

**Notes:** Meaning of the 14-bit field and bit 8 is inferred only from the bit layout.

- Addresses by version: 219: 0x0C08772C
- Called by: `norflash_status_s0_s7`, `norflash_status_s8_s15`, `norflash_wait_busy_or_suspend`, `norflash_write_reg`, `norflash_read_jedec_id`, `norflash_sample_delay_calib`
- Confidence: low

## norflaship_send_cmd_word

**Start a transaction with a raw command word and length (REG_004 bit0 set)**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle, then REG_004 = (param_3 & 0x1FFF) << 12 | (REG_004 & 0xFE000FFF) | 1 and writes REG_000 = param_2. Bit0 appears to mark a transfer with a data phase; param_2 is the already assembled command (opcode and address) word.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | raw command/address word written to REG_000 |
| `param_3` | `u32` | data phase length in bytes (13-bit) |

- Addresses by version: 219: 0x0C0876F4
- Called by: `norflash_wait_busy_or_suspend`, `norflash_reset`, `norflash_write_reg`
- Confidence: medium

## norflaship_set_cfg14_bit3

**Set or clear bit 3 of config register REG_014 (no idle wait)**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). If param_2 != 0 sets REG_014 bit3 (|= 8) else clears it. Unlike its siblings it does not wait for the busy flag.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `s32` | non-zero to set the bit, 0 to clear |

- Addresses by version: 219: 0x0C0878D8
- Called by: `norflash_set_burst_wrap`, `norflash_reset`
- Confidence: low

## norflaship_set_cfg14_bit4

**Set or clear bit 4 of config register REG_014 after waiting for idle**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle; if param_2 != 0 sets REG_014 bit4 (|= 0x10) else clears it.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `s32` | non-zero to set the bit, 0 to clear |

- Addresses by version: 219: 0x0C0878B4
- Called by: `norflash_reset`, `norflash_set_read_mode`, `norflash_erase`
- Confidence: low

## norflaship_set_cfg14_bit5

**Set or clear bit 5 of config register REG_014 after waiting for idle**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle; if param_2 != 0 sets REG_014 bit5 (|= 0x20) else clears it. One of three mode flag bits (bits 3, 4, 5) in REG_014, possibly dual/quad I/O or similar.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `s32` | non-zero to set the bit, 0 to clear |

- Addresses by version: 219: 0x0C087890
- Called by: `norflash_reset`, `norflash_set_read_mode`
- Confidence: low

## norflaship_set_cfg14_byte2

**Set bits 16..23 of config register REG_014 after waiting for idle**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle then replaces REG_014[23:16] with param_2 & 0xFF. Probably the SPI clock divider or sample delay (not confirmed); partner getter is norflaship_get_cfg14_byte2.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | 8-bit value for REG_014[23:16] |

- Addresses by version: 219: 0x0C087838
- Called by: `norflash_apply_dummy_cycles`, `norflash_pre_operation`, `norflash_pre_operation_alt`, `norflash_read_jedec_id`
- Confidence: low

## norflaship_set_cfg14_nibble3

**Set bits 12..15 of config register REG_014 after waiting for idle**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle then REG_014 = ((param_2 << 12) & 0xFFFF) | (REG_014 & 0xFFFF0FFF), replacing the 4-bit field at [15:12]. Likely a sample-delay or dummy-cycle count.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `s16` | 4-bit value for REG_014[15:12] |

- Addresses by version: 219: 0x0C087870
- Called by: `norflash_sample_delay_calib`
- Confidence: low

## norflaship_set_cfg38_width_sel

**Map a size/width value to the 2-bit selector REG_038[14:13]**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Maps param_2 to a code: 8 -> 0, 0x10 -> 1 (0x2000), 0x40 -> 3 (0x6000), anything else -> 2 (0x4000), and writes it into REG_038 bits 14..13 (mask 0xFFFF9FFF). The 8/16/32(default)/64 values look like a bus or burst width in bits.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `s32` | width selector value: 8, 0x10, 0x40, other (treated as 0x20) |

- Addresses by version: 219: 0x0C087978
- Called by: `norflash_set_burst_wrap`
- Confidence: low

## norflaship_set_ctrl_field_4_11

**Set bits 4..11 of flash-IP control register REG_004 after waiting for idle**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Spins until status REG_00C bit0 (busy) is clear, then read-modify-writes REG_004: clears bits 4..11 (mask 0xFFFFF00F) and ORs in (param_2 << 4). The value is not masked, so values above 0xFF would spill into bits 12+. Likely the command/opcode byte or transfer-type field of the pending operation.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | 8-bit field value placed in REG_004[11:4] |

- Addresses by version: 219: 0x0C0875A8
- Called by: `norflash_set_continuous_read`, `norflash_restore_read_config`, `norflash_set_read_mode`, `norflash_post_operation`, `norflash_post_operation_alt`
- Confidence: medium

## norflaship_set_len_and_fill_txfifo

**Program transfer length and push bytes into the TX FIFO**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Writes param_3 & 0x1FFF into REG_004[24:12] (transfer length). Reads the FIFO count field REG_00C[12:8]; if zero returns param_3 without writing anything. Otherwise copies bytes from param_2 to the FIFO register REG_008, at most as many as the count field allows, and returns the number of bytes NOT written (param_3 - count, 0 if everything fit). Used by flash write/program paths.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `ptr` | source byte buffer |
| `param_3` | `u32` | number of bytes / transfer length (13-bit) |

**Returns** `u32`: bytes remaining to send (0 when all were pushed, param_3 when FIFO had no space)

**Notes:** Direction of the FIFO count (free space vs. filled) inferred from use as TX FIFO fill.

- Addresses by version: 219: 0x0C087600
- Called by: `norflash_set_burst_wrap`, `norflash_reset`, `norflash_write_reg`, `norflash_page_program`
- Confidence: medium

## norflaship_set_reg108

**Write a 5-bit value to register REG_108**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Stores param_2 & 0x1F in the register at offset 0x108.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | 5-bit value |

- Addresses by version: 219: 0x0C087A0C
- Called by: `norflash_set_read_mode`
- Confidence: low

## norflaship_set_reg20_byte0

**Set bits 0..7 of register REG_020**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Replaces REG_020[7:0] with param_2, no idle wait.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u8` | 8-bit value for REG_020[7:0] |

- Addresses by version: 219: 0x0C087944
- Called by: `norflash_reset`
- Confidence: low

## norflaship_set_reg20_byte2

**Set bits 16..23 of register REG_020**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Replaces REG_020[23:16] with param_2 & 0xFF, no idle wait. Companion of norflaship_set_reg20_byte0 (opcode/mode bytes for the fast-read command, inferred).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | 8-bit value for REG_020[23:16] |

- Addresses by version: 219: 0x0C087928
- Called by: `norflash_set_read_mode`, `norflash_erase`
- Confidence: low

## norflaship_set_reg30_top_byte

**Write the top byte of a word to register REG_030**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Stores param_2 >> 24 (the most significant byte) in REG_030. Called with an address/opcode word; probably a read-mode command or high address byte register.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | word whose bits 31..24 are written |

- Addresses by version: 219: 0x0C0878F8
- Called by: `norflash_erase`, `norflash_page_program`
- Confidence: low

## norflaship_set_reg40_bits2_3

**Set or clear bits 2..3 (mask 0xC) of register REG_040**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Waits for idle; if param_2 != 0 REG_040 |= 0xC else REG_040 &= ~0xC.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `s32` | non-zero to set both bits, 0 to clear |

- Addresses by version: 219: 0x0C0879E8
- Called by: `norflash_reset`
- Confidence: low

## norflaship_set_xfer_len

**Set transfer length field REG_004[24:12] of the flash IP**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Does REG_004 = (param_2 & 0x1FFF) << 12 | (REG_004 & 0xFE000FFF), without waiting for idle. The 13-bit field holds the number of bytes of the following data phase.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | length in bytes, 13-bit |

- Addresses by version: 219: 0x0C0876B0
- Called by: `norflash_set_continuous_read`
- Confidence: medium

## norflaship_wait_fifo_level

**Busy-wait until REG_00C[7:4] reaches a minimum level**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Spins until ((REG_00C & 0xFF) >> 4) >= param_2. The 4-bit field is a FIFO fill level (probably RX FIFO), so this waits for param_2 entries to be available. No timeout.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |
| `param_2` | `u32` | minimum FIFO level to wait for |

- Addresses by version: 219: 0x0C087790
- Called by: `norflash_status_s0_s7`, `norflash_status_s8_s15`, `norflash_wait_busy_or_suspend`, `norflash_write_reg`, `norflash_read_jedec_id`, `norflash_sample_delay_calib`
- Confidence: medium

## norflaship_wait_idle

**Busy-wait until the flash controller is no longer busy**

Register base = *(u32*)(0x20003060 + id*4), i.e. the per-instance pointer table of the BES NOR-flash controller IP (hal_norflaship style driver; register purpose inferred from access pattern, undocumented). Spins until REG_00C bit0 reads 0. No timeout; the most frequently used helper of this block (12 callers).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | flash-controller instance index (selects base from the pointer table at 0x20003060; only 0 appears used) |

- Addresses by version: 219: 0x0C0877BC
- Called by: `norflash_set_continuous_read`, `norflash_restore_read_config`, `norflash_reset`, `norflash_set_read_mode`, `norflash_pre_operation`, `norflash_pre_operation_alt`, `norflash_post_operation`, `norflash_post_operation_alt`, `norflash_read_jedec_id`, `norflash_sample_delay_calib`, `norflash_erase`, `norflash_page_program`
- Confidence: high

## nvic_clear_pending_irq

**Clear the NVIC pending bit of an external interrupt**

Writes 1 << (irq & 31) to NVIC word (irq >> 5) of the ICPR bank (0xE000E280 + 4*(irq>>5); the decompiler shows it as 0xE000E100 plus 0x60 words). Standard CMSIS NVIC_ClearPendingIRQ. Called from the IRQ-enable helper at 0x0c046f54.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | external IRQ number (0-based, excludes the 16 core exceptions) |

- Addresses by version: 219: 0x0C03AA9C
- Peripheral registers: `0xe000e100` (A)
- Called by: `hal_irq_install_handler`
- Confidence: high

## nvic_disable_irq

**Disable an external interrupt in the NVIC**

Writes 1 << (irq & 31) to the ICER bank (0xE000E180 + 4*(irq>>5); decompiler shows 0xE000E100 + 0x20 words). CMSIS NVIC_DisableIRQ. Caller is the IRQ-disable helper at 0x0c046f7c.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | external IRQ number |

- Addresses by version: 219: 0x0C03AAE0
- Peripheral registers: `0xe000e100` (A)
- Called by: `hal_irq_remove_handler`
- Confidence: high

## nvic_set_default_priority_and_enable_irq

**Set IRQ priority to 0x60 and enable it in the NVIC**

If irq < 0xF0, writes priority byte 0x60 to NVIC IPR[irq] (0xE000E400 + irq); the value 0x60 corresponds to the third of the top priority levels if 3 priority bits are implemented (levels sit above BASEPRI 0x40 used by the RTOS critical sections, so these IRQs are masked when BASEPRI=0x40). It then writes 1 << (irq & 31) to ISER[irq >> 5] (0xE000E100) to enable the interrupt. Equivalent to NVIC_SetPriority(irq,0x60) + NVIC_EnableIRQ(irq); does not clear the pending bit.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | external IRQ number |

**Notes:** Priority-level interpretation depends on the number of implemented priority bits (not checked).

- Addresses by version: 219: 0x0C03AAB8
- Peripheral registers: `0xe000e100` (A), `0xe000e400` (A)
- Called by: `hal_irq_install_handler`
- Confidence: high

## pm_busy_mask_clear_bit

**Clear bit n in the global bitmask DAT_2000aa6c (n < 32)**

If param_1 < 32, clears bit param_1 of the 32-bit mask DAT_2000aa6c inside a BASEPRI critical section and returns 0; otherwise returns 1 without changes. Counterpart of pm_busy_mask_set_bit (0x0c031c40). Called by the I2C bit-release path (0x0c030268, bit 2) and the IPC ISR (0x0c0314f0, bit 0). The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40 when privileged; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is restored afterwards).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit index 0..31 |

**Returns** `u32`: 0 on success, 1 if the index is out of range

**Notes:** Name/role of the mask is a guess (looks like a set of activity/sleep-veto flags); only the bit manipulation is certain.

- Addresses by version: 219: 0x0C031C90
- Called by: `hal_i2c_clear_busy`, `hal_sysipc_tx_done_irq_handler`
- Confidence: low

## pm_busy_mask_set_bit

**Set bit n in the global bitmask DAT_2000aa6c (n < 32)**

If param_1 < 32, sets bit param_1 of the 32-bit mask DAT_2000aa6c inside a BASEPRI critical section and returns 0; otherwise returns 1 without changes. Counterpart of pm_busy_mask_clear_bit (0x0c031c90). Called by the IPC send path (0x0c031884) and the platform init (0x0c03ac44, which sets bit 0x1f). The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40 when privileged; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is restored afterwards).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit index 0..31 |

**Returns** `u32`: 0 on success, 1 if the index is out of range

**Notes:** Name/role of the mask is a guess (looks like a set of activity/sleep-veto flags); only the bit manipulation is certain.

- Addresses by version: 219: 0x0C031C40
- Called by: `hal_sysipc_send`, `ble_219_0c03ac44`
- Confidence: low

## pm_wake_mask_clear_bit

**Clear bit n in the global bitmask DAT_2000aa68 (n < 32)**

If param_1 < 32, clears bit param_1 of the 32-bit mask DAT_2000aa68 inside a BASEPRI critical section and returns 0; otherwise returns 1 without changes. Counterpart of pm_wake_mask_set_bit (0x0c031cdc). Called by 0x0c02f73c when the last user is removed. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40 when privileged; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is restored afterwards).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit index 0..31 |

**Returns** `u32`: 0 on success, 1 if the index is out of range

**Notes:** Name/role of the mask is a guess (looks like a set of activity/sleep-veto flags); only the bit manipulation is certain.

- Addresses by version: 219: 0x0C031D2C
- Called by: `ble_219_0c02f73c`
- Confidence: low

## pm_wake_mask_set_bit

**Set bit n in the global bitmask DAT_2000aa68 (n < 32)**

If param_1 < 32, sets bit param_1 of the 32-bit mask DAT_2000aa68 inside a BASEPRI critical section and returns 0; otherwise returns 1 without changes. Counterpart of pm_wake_mask_clear_bit (0x0c031d2c). Called by 0x0c02f73c when the first user of a shared resource (tracked in DAT_2000a60c) is added. The body runs inside a BASEPRI critical section (BASEPRI raised to 0x40 when privileged; if it was not already 0x40 the call-site address and LR are logged to DAT_20003d70/DAT_20003d74, and DAT_20003d70 is reset to 0xffffffff on exit when BASEPRI was 0 on entry; BASEPRI is restored afterwards).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | bit index 0..31 |

**Returns** `u32`: 0 on success, 1 if the index is out of range

**Notes:** Name/role of the mask is a guess (looks like a set of activity/sleep-veto flags); only the bit manipulation is certain.

- Addresses by version: 219: 0x0C031CDC
- Called by: `ble_219_0c02f73c`
- Confidence: low

## systick_measure_loop_us

**Time a busy loop of param_1 iterations with SysTick and return the duration in microseconds (or -1 on wrap)**

Configures SysTick: CTRL = 0, VAL = 0, LOAD = 0xFFFFFF, CTRL = 1 (enable, external reference clock, no interrupt), spins param_1 iterations of a decrement loop, then reads VAL and CTRL. If COUNTFLAG (bit 16) is set the counter wrapped and 0xFFFFFFFF is returned; otherwise it returns ((~VAL & 0xFFFFFF) * 1000) / (freq / 1000) = elapsed ticks * 1e6 / freq microseconds, freq being the SysTick reference clock from ble_ram_patch_thunk_20000554. Called from the BogoMIPS calibration 0x0c035da4 ('Calculate BogoMips loop...'), which halves the loop count until no wrap occurs and stores loops-per-microsecond in DAT_20003e90 (initial .data value 0x68).

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `u32` | number of loop iterations to time |

**Returns** `u32`: elapsed microseconds, 0xFFFFFFFF if the 24-bit counter wrapped

**Notes:** Leaves SysTick running with LOAD = 0xFFFFFF; vPortSetupTimerInterrupt reprograms it afterwards.

- Addresses by version: 219: 0x0C03F7CC
- Peripheral registers: `0xe000e010` (RW), `0xe000e014` (W), `0xe000e018` (RW)
- Called by: `ble_219_0c035da4`
- Calls: `ble_ram_patch_thunk_20000554`
- Confidence: high

## thunk_bes_gpio_read_status_words

**Tail-branch thunk to bes_gpio_read_status_words (0x0c041ab0)**

Single-instruction trampoline that jumps to bes_gpio_read_status_words with its arguments unchanged: copies up to three 32-bit words from 0x4008508c, 0x40085090 and (0x40085094 & 0xffff) into param_1 and returns min(param_2, 3). Exists as a separate symbol (probably a linker-level alias or veneer). Called from 0x0c02feec.

| Parameter | Type | Description |
|---|---|---|
| `param_1` | `ptr` | u32 out buffer for up to 3 status words |
| `param_2` | `u32` | number of words requested |

**Returns** `u32`: min(param_2, 3), number of words written

- Addresses by version: 219: 0x0C041B5C
- Called by: `hal_gpio_irq_handler`
- Calls: `bes_gpio_read_status_words`
- Confidence: high
