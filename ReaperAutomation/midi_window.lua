-- Auto Answer 'MIDI File Import' dialog
-- Start this script before inserting media
-- v1.01

function Main()
  local hwnd = reaper.JS_Window_FindTop('MIDI File Import', true)
  if hwnd then -- get checkbox handles
    local chk_box1 = reaper.JS_Window_FindChildByID(hwnd, 0x412)
    local chk_box2 = reaper.JS_Window_FindChildByID(hwnd, 0x413)
    --local chk_box3 = reaper.JS_Window_FindChildByID(hwnd, 0x414)

    -- set checked state of check boxes
    reaper.JS_WindowMessage_Send(chk_box1, "BM_SETCHECK", 0x0, 0,0,0) -- 0x0=BST_UNCHECKED -- not checked
    reaper.JS_WindowMessage_Send(chk_box2, "BM_SETCHECK", 0x0, 0,0,0) -- 0x1=BST_CHECKED   -- checked

    -- click OK button
    reaper.JS_WindowMessage_Send(hwnd, "WM_COMMAND", 0x1,0,0,0)
    -- return -- OPTIONAL - Enable to exit script after answering dialog
  end
  reaper.defer(Main)
end

Main()
